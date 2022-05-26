from enum import Enum


class CPUID_INSTRUCTIONS(Enum):
    #================================================
    #
    #             FEATURES STORED IN EAX
    #
    #================================================
    DTS_CAPAB       = (6, 0, 0, 0)#                  -- Digital Thermal Sensor (DTS) capability
    ITB_TECH_CAPAB  = (6, 0, 0, 1)#                  -- Intel Turbo Boost Technology capability
    ARAT_CAPAB      = (6, 0, 0, 2)#                  -- Always Running APIC Timer (ARAT) capability
    #               = (6, 0, 0, 3)#                  -- <RESERVED IN EAX, WHEN EAX=6>
    PLN_CAPAB       = (6, 0, 0, 4)#                  -- Power Limit Notification (PLN) capability
    ECMD_CAPAB      = (6, 0, 0, 5)#                  -- Extended Clock Modulation Duty (ECMD) capability
    PTM_CAPAB       = (6, 0, 0, 6)#                  -- Package Thermal Management (PTM) capability
    #               = (6, 0, 0, 7)                   -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 8)                   -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 9)                   -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 11)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 12)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 13)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 14)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 15)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 16)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 17)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 18)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 19)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 20)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 21)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 22)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 23)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 24)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 25)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 26)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 27)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 28)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 29)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 30)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (6, 0, 0, 31)                  -- <RESERVED IN EAX, WHEN EAX=6>
    #               = (7, 1, 0, 0)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 1)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 2)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 3)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 4)                   -- <RESERVED IN EAX, WHEN EAX=7>
    AVX512_BF16     = (7, 1, 0, 5)#                  -- AVX-512 BFLOAT16 instructions
    #               = (7, 1, 0, 6)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 7)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 8)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 9)                   -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 10)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 11)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 12)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 13)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 14)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 15)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 16)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 17)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 18)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 19)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 21)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 22)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 23)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 24)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 25)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 26)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 27)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 28)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 29)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 30)                  -- <RESERVED IN EAX, WHEN EAX=7>
    #               = (7, 1, 0, 31)                  -- <RESERVED IN EAX, WHEN EAX=7>


    #================================================
    #
    #             FEATURES STORED IN EBX
    #
    #================================================
    FSGSBASE        = (7, 0, 1, 0)#                  -- Access to base of %fs and %gs
    IA32_TSC_ADJ    = (7, 0, 1, 1)#                  -- <No description provided>
    SGX             = (7, 0, 1, 2)#                  -- Software Guard Extensions
    BMI1            = (7, 0, 1, 3)#                  -- Bit Manipulation Instruction Set 1
    HLE             = (7, 0, 1, 4)#                  -- TSX Hardware Lock Elision
    AVX2            = (7, 0, 1, 5)#                  -- Advanced Vector Extensions 2
    FDP_EXCPTN_ONLY = (7, 0, 1, 6)#                  -- <No description provided>
    SMEP            = (7, 0, 1, 7)#                  -- Supervisor Mode Execution Prevention
    BMI2            = (7, 0, 1, 8)#                  -- Bit Manipulation Instruction Set 2
    ERMS            = (7, 0, 1, 9)#                  -- Enhanced REP MOVSB/STOSB
    INVPCID         = (7, 0, 1, 10)#                 -- INVPCID instruction
    RTM             = (7, 0, 1, 11)#                 -- TSX Restricted Transactional Memory
    PQM             = (7, 0, 1, 12)#                 -- Platform Quality of Service Monitoring
    FPU_CS_DS_DEPR  = (7, 0, 1, 13)#                 -- FPU CS and FPU DS deprecated
    MPX             = (7, 0, 1, 14)#                 -- Intel MPX (Memory Protection Extensions)
    PQE             = (7, 0, 1, 15)#                 -- Platform Quality of Service Enforcement
    AVX512_F        = (7, 0, 1, 16)#                 -- AVX-512 Foundation
    AVX512_DQ       = (7, 0, 1, 17)#                 -- AVX-512 Doubleword and Quadword Instructions
    RDSEED          = (7, 0, 1, 18)#                 -- RDSEED instruction
    ADX             = (7, 0, 1, 19)#                 -- Intel ADX (Multi-Precision Add-Carry Instruction Extensions)
    SMAP            = (7, 0, 1, 20)#                 -- Supervisor Mode Access Prevention
    AVX512_IFMA     = (7, 0, 1, 21)#                 -- AVX-512 Integer Fused Multiply-Add Instructions
    PCOMMIT         = (7, 0, 1, 22)#                 -- PCOMMIT instruction
    CLFLUSHOPT      = (7, 0, 1, 23)#                 -- CLFLUSHOPT instruction
    CLWB            = (7, 0, 1, 24)#                 -- CLWB instruction
    INTEL_PT        = (7, 0, 1, 25)#                 -- Intel Processor Trace
    AVX512_PF       = (7, 0, 1, 26)#                 -- AVX-512 Prefetch Instructions
    AVX512_ER       = (7, 0, 1, 27)#                 -- AVX-512 Exponential and Reciprocal Instructions
    AVX512_CD       = (7, 0, 1, 28)#                 -- AVX-512 Conflict Detection Instructions
    SHA             = (7, 0, 1, 29)#                 -- Intel SHA extensions
    AVX512_BW       = (7, 0, 1, 30)#                 -- AVX-512 Byte and Word Instructions
    AVX512_VL       = (7, 0, 1, 31)#                 -- AVX-512 Vector Length Extensions


    #================================================
    #
    #             FEATURES STORED IN ECX
    #
    #================================================
    SSE3            = (1, 0, 2, 0)#                  -- Prescott New Instructions - SSE3 (PNI)
    PCLMULQDQ       = (1, 0, 2, 1)#                  -- PCLMULQDQ
    DTES64          = (1, 0, 2, 2)#                  -- 64-bit debug store (edx bit 21)
    MONITOR         = (1, 0, 2, 3)#                  -- MONITOR and MWAIT instructions (SSE3)
    DS_CPL          = (1, 0, 2, 4)#                  -- CPL qualified debug store
    VMX             = (1, 0, 2, 5)#                  -- Virtual Machine eXtensions
    SMX             = (1, 0, 2, 6)#                  -- Safer mode Extensions (LaGrande) 
    EST             = (1, 0, 2, 7)#                  -- Enhanced SpeedStep
    TM2             = (1, 0, 2, 8)#                  -- Thermal Monitor 2
    SSSE3           = (1, 0, 2, 9)#                  -- Supplemental SSE3 instructions
    CNXT_ID         = (1, 0, 2, 10)#                 -- L1 Context ID
    SDBG            = (1, 0, 2, 11)#                 -- Silicon Debug interface
    FMA             = (1, 0, 2, 12)#                 -- Fused multiply-add (FMA3)
    CX16            = (1, 0, 2, 13)#                 -- CMPXCHG16B instruction
    XTPR            = (1, 0, 2, 14)#                 -- Can disable sending task priority messages
    PDCM            = (1, 0, 2, 15)#                 -- Perfmon & debug capability
    #               = (1, 0, 2, 16)                  -- <RESERVED IN ECX, WHEN EAX=1>
    PCID            = (1, 0, 2, 17)#                 -- Process context identifiers (CR4 bit 17)
    DCA             = (1, 0, 2, 18)#                 -- Direct cache access for DMA writes
    SSE4_1          = (1, 0, 2, 19)#                 -- SSE4.1 instructions
    SSE4_2          = (1, 0, 2, 20)#                 -- SSE4.2 instructions
    X2APIC          = (1, 0, 2, 21)#                 -- x2APIC
    MOVBE           = (1, 0, 2, 22)#                 -- MOVBE instruction (big-endian)
    POPCNT          = (1, 0, 2, 23)#                 -- POPCNT instruction
    TSC_DL          = (1, 0, 2, 24)#                 -- APIC implements one-shot operation using a TSC deadline value
    AES             = (1, 0, 2, 25)#                 -- AES instruction set
    XSAVE           = (1, 0, 2, 26)#                 -- XSAVE, XRESTOR, XSETBV, XGETBV
    OSXSAVE         = (1, 0, 2, 27)#                 -- XSAVE enabled by OS
    AVX             = (1, 0, 2, 28)#                 -- Advanced Vector Extensions
    F16C            = (1, 0, 2, 29)#                 -- F16C (half-precision) FP feature
    RDRND           = (1, 0, 2, 30)#                 -- RDRAND (on-chip random number generator) feature
    HYPERVISOR      = (1, 0, 2, 31)#                 -- Hypervisor present (always zero on physical CPUs)
    HCF_CAPAB       = (6, 0, 2, 0)#                  -- Hardware Coordination Feedback capability
    ACNT2_CAPAB     = (6, 0, 2, 1)#                  -- ACNT2 Capability
    #               = (6, 0, 2, 2)                   -- <RESERVED IN ECX, WHEN EAX=6>
    PEB_CAPAB       = (6, 0, 2, 3)#                  -- Performance-Energy Bias capability
    #               = (6, 0, 0, 4)                   -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 5)                   -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 6)                   -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 7)                   -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 8)                   -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 9)                   -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 11)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 12)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 13)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 14)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 15)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 16)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 17)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 18)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 19)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 20)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 21)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 22)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 23)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 24)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 25)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 26)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 27)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 28)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 29)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 30)                  -- <RESERVED IN ECX, WHEN EAX=6>
    #               = (6, 0, 0, 31)                  -- <RESERVED IN ECX, WHEN EAX=6>
    PREFETCHWT1     = (7, 0, 2, 0)#                  -- PREFETCHWT1 instruction
    AVX512_VBMI     = (7, 0, 2, 1)#                  -- AVX-512 Vector Bit Manipulation Instructions
    UMIP            = (7, 0, 2, 2)#                  -- User-mode Instruction Prevention
    PKU             = (7, 0, 2, 3)#                  -- Memory Protection Keys for User-mode pages
    OSPKE           = (7, 0, 2, 4)#                  -- PKU enabled by OS
    WAITPKG         = (7, 0, 2, 5)#                  -- Timed pause and user-level monitor/wait
    AVX512_VBMI2    = (7, 0, 2, 6)#                  -- AVX-512 Vector Bit Manipulation Instructions 2
    CET_SS          = (7, 0, 2, 7)#                  -- Control flow enforcement (CET) shadow stack
    GFNI            = (7, 0, 2, 8)#                  -- Galois Field instructions
    VAES            = (7, 0, 2, 9)#                  -- Vector AES instruction set (VEX-256/EVEX)
    VPCLMULQDQ      = (7, 0, 2, 10)#                 -- CLMUL instruction set (VEX-256/EVEX)
    AVX512_VNNI     = (7, 0, 2, 11)#                 -- AVX-512 Vector Neural Network Instructions
    AVX512_BITALG   = (7, 0, 2, 12)#                 -- AVX-512 BITALG instructions
    TME_EN          = (7, 0, 2, 13)#                 -- IA32_TME related MSRs are supported
    AVX512_POPCNTDQ = (7, 0, 2, 14)#                 -- AVX-512 Vector Population Count Double and Quad-word (AVX512_VPOPCNTDQ)
    #               = (7, 0, 2, 15)                  -- <RESERVED IN ECX, WHEN EAX=7>
    _5LVLPGIN       = (7, 0, 2, 16)#                 -- 5-level paging
    MAWAU           = [#                             -- The value of userspace MPX Address-Width Adjust used by the BNDLDX and BNDSTX Intel MPX instructions in 64-bit mode
                      (7, 0, 2, 17),
                      (7, 0, 2, 18),
                      (7, 0, 2, 19),
                      (7, 0, 2, 20),
                      (7, 0, 2, 21)
                    ]
    RDPID           = (7, 0, 2, 22)#                 -- Read Processor ID and IA32_TSC_AUX
    KL              = (7, 0, 2, 23)#                 -- Key Locker
    #               = (7, 0, 2, 24)                  -- <RESERVED IN ECX, WHEN EAX=7>
    CLDEMOTE        = (7, 0, 2, 25)#                 -- Cache line demote
    #               = (7, 0, 2, 26)                  -- <RESERVED IN ECX, WHEN EAX=7>
    MOVDIRI         = (7, 0, 2, 27)#                 -- <No description provided>
    MOVDIR64B       = (7, 0, 2, 28)#                 -- <No description provided>
    ENQCMD          = (7, 0, 2, 29)#                 -- Enqueue Stores
    SGX_LC          = (7, 0, 2, 30)#                 -- SGX Launch Configuration
    PKS             = (7, 0, 2, 31)#                 -- Protection keys for supervisor-mode pages
    LAHF_IM         = (0x80000001, 0, 2, 0)#         -- LAHF/SAHF in long mode
    CMP_LEGACY      = (0x80000001, 0, 2, 1)#         -- Hyperthreading not valid
    SVM             = (0x80000001, 0, 2, 2)#         -- Secure Virtual Machine
    EXTAPIC         = (0x80000001, 0, 2, 3)#         -- Extended APIC space
    CR8_LEGACY      = (0x80000001, 0, 2, 4)#         -- CR8 in 32-bit mode
    ABM             = (0x80000001, 0, 2, 5)#         -- Advanced bit manipulation (lzcnt and popcnt)
    SSE4A           = (0x80000001, 0, 2, 6)#         -- SSE4a
    MISALIGNSSE     = (0x80000001, 0, 2, 7)#         -- Misaligned SSE mode
    _3DNOWPREFETCH  = (0x80000001, 0, 2, 8)#         -- PREFETCH and PREFETCHW instructions
    OSVW            = (0x80000001, 0, 2, 9)#         -- OS Visible Workaround
    IBS             = (0x80000001, 0, 2, 10)#        -- Instruction Based Sampling
    XOP             = (0x80000001, 0, 2, 11)#        -- XOP instruction set
    SKINIT          = (0x80000001, 0, 2, 12)#        -- SKINIT/STGI instructions
    WDT             = (0x80000001, 0, 2, 13)#        -- Watchdog timer
    #               = (0x80000001, 0, 2, 14)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    LWP             = (0x80000001, 0, 2, 15)#        -- Light Weight Profiling
    FMA4            = (0x80000001, 0, 2, 16)#        -- 4 operands fused multiply-add
    TCE             = (0x80000001, 0, 2, 17)#        -- Translation Cache Extension
    #               = (0x80000001, 0, 2, 18)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    NODEID_MSR      = (0x80000001, 0, 2, 19)#        -- NodeID MSR
    #               = (0x80000001, 0, 2, 20)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    TBM             = (0x80000001, 0, 2, 21)#        -- Trailing Bit Manipulation
    TOPOEXT         = (0x80000001, 0, 2, 22)#        -- Topology Extensions
    PERFCTR_CORE    = (0x80000001, 0, 2, 23)#        -- Core performance counter extensions
    PERFCTR_NB      = (0x80000001, 0, 2, 24)#        -- NB performance counter extensions
    #               = (0x80000001, 0, 2, 25)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    DBX             = (0x80000001, 0, 2, 26)#        -- Data breakpoint extensions
    PERFTSC         = (0x80000001, 0, 2, 27)#        -- Performance TSC
    PCX_L2I         = (0x80000001, 0, 2, 28)#        -- L2I perf counter extensions
    #               = (0x80000001, 0, 2, 29)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    #               = (0x80000001, 0, 2, 30)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    #               = (0x80000001, 0, 2, 31)         -- <RESERVED IN ECX, WHEN EAX=800000001h>
    

    #================================================
    #
    #             FEATURES STORED IN EDX
    #
    #================================================
    FPU             = (1, 0, 3, 0)#                  -- Onboard x87 FPU 
    VME             = (1, 0, 3, 1)#                  -- Virtual 8086 mode extensions (such as VIF, VIP, PIV)
    DE              = (1, 0, 3, 2)#                  -- Debugging extensions (CR4 bit 3)
    PSE             = (1, 0, 3, 3)#                  -- Page Size Extension
    TSC             = (1, 0, 3, 4)#                  -- Time Stamp Counter
    MSR             = (1, 0, 3, 5)#                  -- Model-specific registers
    PAE             = (1, 0, 3, 6)#                  -- Physical Address Extension
    MCE             = (1, 0, 3, 7)#                  -- Machine Check Exception
    CX8             = (1, 0, 3, 8)#                  -- CMPXCHG8 (compare-and-swap) instruction
    APIC            = (1, 0, 3, 9)#                  -- Onboard Advanced Programmable Interrupt Controller
    #               = (1, 0, 3, 10)                  -- <RESERVED IN EDX>
    SEP             = (1, 0, 3, 11)#                 -- SYSENTER and SYSEXIT instructions
    MTRR            = (1, 0, 3, 12)#                 -- Memory Type Range Registers
    PGE             = (1, 0, 3, 13)#                 -- Page Global Enable bit in CR4
    MCA             = (1, 0, 3, 14)#                 -- Machine check architecture
    CMOV            = (1, 0, 3, 15)#                 -- Conditional move and FCMOV instructions
    PAT             = (1, 0, 3, 16)#                 -- Page Attribute Table
    PSE36           = (1, 0, 3, 17)#                 -- 36-bit page size extension
    PSN             = (1, 0, 3, 18)#                 -- Processor Serial Number
    CLFSH           = (1, 0, 3, 19)#                 -- CLFLUSH instruction (SSE2)
    #               = (1, 0, 3, 20)                  -- <RESERVED IN EDX, WHEN EAX=1>
    DS              = (1, 0, 3, 21)#                 -- Debug store: save trace of executed jumps
    ACPI            = (1, 0, 3, 22)#                 -- Onboard thermal control MSRs for ACPI
    MMX             = (1, 0, 3, 23)#                 -- MMX instructions
    FXSR            = (1, 0, 3, 24)#                 -- FXSAVE, FXRESTOR instructions (CR4 bit 9)
    SSE             = (1, 0, 3, 25)#                 -- SSE instructions (aka, Katmai New Instructions)
    SSE2            = (1, 0, 3, 26)#                 -- SSE2 instructions
    SS              = (1, 0, 3, 27)#                 -- CPU cache implements self-snoop
    HTT             = (1, 0, 3, 28)#                 -- Hyper-threading
    TM              = (1, 0, 3, 29)#                 -- Thermal monitor automatically limits temperature
    IA64            = (1, 0, 3, 30)#                 -- IA64 processor emulating x86
    PBE             = (1, 0, 3, 31)#                 -- Pending Break Enable (PBE# pin) wakeup capability
    #               = (7, 0, 3, 0)                   -- <RESERVED IN EDX, WHEN EAX=7>
    #               = (7, 0, 3, 1)                   -- <RESERVED IN EDX, WHEN EAX=7>
    AVX512_4VNNIW   = (7, 0, 3, 2)#                  -- AVX-512 4-register Neural Network Instructions
    AVX512_4FMAPS   = (7, 0, 3, 3)#                  -- AVX-512 4-register Multiply Accumulation Single precision
    FSRM            = (7, 0, 3, 4)#                  -- Fast Short REP MOVSB
    #               = (7, 0, 3, 5)                   -- <RESERVED IN EDX, WHEN EAX=7>
    #               = (7, 0, 3, 6)                   -- <RESERVED IN EDX, WHEN EAX=7>
    #               = (7, 0, 3, 7)                   -- <RESERVED IN EDX, WHEN EAX=7>
    AVX512_VP2ISCT  = (7, 0, 3, 8)#                  -- AVX-512 VP2INTERSECT Doubleword and Quadword Instructions
    SRBDS_CTRL      = (7, 0, 3, 9)#                  -- Special Register Buffer Data Sampling Mitigations
    MD_CLEAR        = (7, 0, 3, 10)#                 -- VERW instructions clears CPU buffers
    RTM_ALWAYS_ABRT = (7, 0, 3, 11)#                 -- ALL TSX transactions are aborted (RTM_ALWAYS_ABORT)
    #               = (7, 0, 3, 12)                  -- <RESERVED IN EDX, WHEN EAX=7>
    TSX_FORCE_ABRT  = (7, 0, 3, 13)#                 -- TSX_FORCE_ABORT MSR is available
    SERIALIZE       = (7, 0, 3, 14)#                 -- Serialize instruction execution
    HYBRID          = (7, 0, 3, 15)#                 -- Mixture of CPU types in processor topology
    TSXLDTRK        = (7, 0, 3, 16)#                 -- TSX suspend load address tracking
    #               = (7, 0, 3, 17)                  -- <RESERVED IN EDX, WHEN EAX=7>
    PCONFIG         = (7, 0, 3, 18)#                 -- Platform configuration (Memory Encryption Technologies Instructions)
    LBR             = (7, 0, 3, 19)#                 -- Architectural Last Branch Records
    CET_IBT         = (7, 0, 3, 20)#                 -- Control flow enforcement (CET) indirect branch tracking
    #               = (7, 0, 3, 21)                  -- <RESERVED IN EDX, WHEN EAX=7>
    AMX_BF16        = (7, 0, 3, 22)#                 -- Tile computation on bfloat16 numbers
    AVX512_FP16     = (7, 0, 3, 23)#                 -- AVX512-FP16 half-precision floating-point instructions
    AMX_TILE        = (7, 0, 3, 24)#                 -- Tile architecture
    AMX_INT8        = (7, 0, 3, 25)#                 -- Tile computation on 8-bit integers
    SPEC_CTRL       = (7, 0, 3, 26)#                 -- Speculation Control, part of IBC: IBRS and IBPB (Alias: IBRS_IBPB)
    STIBP           = (7, 0, 3, 27)#                 -- Single Thread indirect Branch Predictor, part of IBC
    L1D_FLUSH       = (7, 0, 3, 28)#                 -- IA32_FLUSH_CMD MSR
    IA32_ARCH_CAPAB = (7, 0, 3, 29)#                 -- Speculative Side Channel Mitigations (IA32_ARCH_CAPABILITIES)
    IA32_CORE_CAPAB = (7, 0, 3, 30)#                 -- Support for an MSR listing model-specific core capabilities (IA32_CORE_CAPABILITIES)
    SSBD            = (7, 0, 3, 31)#                 -- Speculative Store Bypass Disable, as mitigation for Speculative Store Bypass (IA32_SPEC_CTRL)
  # FPU             = (0x80000001, 0, 3, 0)          -- Onboard x87 FPU
  # VME             = (0x80000001, 0, 3, 1)          -- Virtual 8086 mode extensions (such as VIF, VIP, PIV)
  # DE              = (0x80000001, 0, 3, 2)          -- Debugging extensions (CR4 bit 3)
  # PSE             = (0x80000001, 0, 3, 3)          -- Page Size Extension
  # TSC             = (0x80000001, 0, 3, 4)          -- Time Stamp Counter
  # MSR             = (0x80000001, 0, 3, 5)          -- Model-specific registers
  # PAE             = (0x80000001, 0, 3, 6)          -- Physical Address Extension
  # MCE             = (0x80000001, 0, 3, 7)          -- Machine Check Exception
  # CX8             = (0x80000001, 0, 3, 8)          -- CMPXCHG8 (compare-and-swap) instruction
  # APIC            = (0x80000001, 0, 3, 9)          -- Onboard Advanced Programmable Interrupt Controller
  #                 = (0x80000001, 0, 3, 10)         -- <RESERVED IN EDX, WHEN EAX=80000001h>
    SYSCALL         = (0x80000001, 0, 3, 11)#        -- SYSCALL and SYSRET instructions
  # MTRR            = (0x80000001, 0, 3, 12)         -- Memory Type Range Registers
  # PGE             = (0x80000001, 0, 3, 13)         -- Page Global Enable bit in CR4
  # MCA             = (0x80000001, 0, 3, 14)         -- Machine check architecture
  # CMOV            = (0x80000001, 0, 3, 15)         -- Conditional move and FCMOV instructions
  # PAT             = (0x80000001, 0, 3, 16)         -- Page Attribute Table
  # PSE36           = (0x80000001, 0, 3, 12)         -- 36-bit page size extension
  #                 = (0x80000001, 0, 3, 18)         -- <RESERVED IN EDX, WHEN EAX=80000001h>
    MP              = (0x80000001, 0, 3, 19)#        -- Multiprocessor Capable
    NX              = (0x80000001, 0, 3, 20)#        -- NX bit
  #                 = (0x80000001, 0, 3, 21)         -- <RESERVED IN EDX, WHEN EAX=80000001h>
    MMXEXT          = (0x80000001, 0, 3, 22)#        -- Extended MMX
  # MMX             = (0x80000001, 0, 3, 23)         -- MMX instructions
  # FXSR            = (0x80000001, 0, 3, 24)         -- FXSAVE, FXRSTOR instructions (CR4 bit 9)
    FXSR_OPT        = (0x80000001, 0, 3, 25)#        -- FXSAVE/FXRSTOR optimizations
    PDPE1GB         = (0x80000001, 0, 3, 26)#        -- Gigabyte pages
    RDTSCP          = (0x80000001, 0, 3, 27)#        -- RDTSCP instruction
  #                 = (0x80000001, 0, 3, 28)         -- <RESERVED IN EDX, WHEN EAX=80000001h>
    LM              = (0x80000001, 0, 3, 29)#        -- Long mode
    _3DNOWEXT       = (0x80000001, 0, 3, 30)#        -- Extended 3DNow!
    _3DNOW          = (0x80000001, 0, 3, 31)#        -- 3DNow!