class InputUtil:
    PS2_KEYBOARD_IDS = [
        "PNP0303",
        "PNP030B",
        "PNP0320",
    ]

    PS2_MOUSE_IDS = [
        "PNP0F03",
        "PNP0F0B",
        "PNP0F0E",
        "PNP0F12",
        "PNP0F13",
    ]

    def __is_ps2_keyboard(ids):
        for id in InputUtil.PS2_KEYBOARD_IDS:
            if id in ids:
                return True

        return False

    def __is_ps2_mouse(ids):
        for id in InputUtil.PS2_MOUSE_IDS:
            if id in ids:
                return True

        return False

    def get_protocol(pnpid, _wmi) -> str | None:
        """ Obtains the parent driver/protocol type for the given input device (WINDOWS ONLY.) """

        from pysi.util.util import Util

        if Util.get_kernel().get("os") != "Windows":
            return

        from ctypes import c_ulong
        from pysi.interops.cfgmgr32.core.cfgmgr32 import CM32
        from pysi.interops.cfgmgr32.util.get_info import get_info
        from wmi import WMI

        if (
            not _wmi or 

            # Shallow check to ensure the provided
            # value is an actual _wmi_object instance.
            not getattr(_wmi, "instances", False)
        ):
            _wmi = WMI()

        cm32 = CM32()
        pdnDevInst = c_ulong()

        # Status code 0 means success,
        # if it's a different code - something went wrong.
        if (
            cm32.CM_Locate_DevNodeA(
                pdnDevInst,
                pnpid.encode("UTF8")
            ).get("code") != 0x0
        ):
            return

        parentInst = c_ulong()

        # Status code 0 means success,
        # if it's a different code - something went wrong.
        if (
            cm32.CM_Get_Parent(
                parentInst,
                pdnDevInst
            ).get("code") != 0x0
        ):
            return

        device = get_info(pdnDevInst, cm32)
        parent = get_info(parentInst, cm32)

        dev_name = device.get("name", "")
        prnt_name = parent.get("name", "")

        dev_driver = device.get("driver_desc", "")
        prnt_driver = parent.get("driver_desc", "")

        if (
            "i2c" in dev_name.lower() or
            "i2c" in prnt_name.lower()
        ):
            return "I2C"

        elif (
            "usb" in dev_driver.lower() or
            "usb" in prnt_driver.lower()
        ):
            return "USB"

        else:
            # Massive thank you to https://github.com/1Revenger1
            # for writing the logic for distinguishing SMBus and PS/2.

            compatible_ids = device.get("compatible_ids", "")

            if InputUtil.__is_ps2_keyboard(compatible_ids):
                return "PS/2"

            if not InputUtil.__is_ps2_mouse(compatible_ids):
                return

            smbus_driver = InputUtil.get_smbus_driver(_wmi)

            # This should never happen.
            if not smbus_driver:
                return "PS/2"

            name = smbus_driver.wmi_property("Name").value

            if (
                ("synaptics" in name.lower() and
                 "synaptics" in dev_name.lower()) or
                ("elans" in name.lower() and
                 "elans" in dev_name.lower())
            ):
                return "SMBus"
            
            return "PS/2"

    def get_smbus_driver(_wmi):
        """ Obtains the SMBus driver (WINDOWS ONLY.) """

        from pysi.util.util import Util
        from wmi import WMI

        if Util.get_kernel().get("os") != "Windows":
            return

        if (
            not _wmi or 

            # Shallow check to ensure the provided
            # value is an actual _wmi_object instance.
            not getattr(_wmi, "instances", False)
        ):
            _wmi = WMI()

        # This can take a few seconds on systems
        # that might have quite a few input devices...
        #
        # That is, unless the user implements the logic for themselves
        # and doesn't use the "prebuilt" `InputManager` instance.
        for entity in _wmi.instances("Win32_PnPEntity"):
            compat_id = entity.wmi_property("CompatibleID").value

            if (
                compat_id and
                type(compat_id) != str and
                "PCI\\CC_0C0500" in compat_id
            ):
                return entity

        return
