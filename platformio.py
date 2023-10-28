Import("env")

C_DEFS = [
    "-DCORE_CM7",
    "-DSTM32H750xx",
    "-DSTM32H750IB",
    "-DARM_MATH_CM7",
    "-Dflash_layout",
    "-DHSE_VALUE=16000000",
    "-DUSE_HAL_DRIVER",
    "-DUSE_FULL_LL_DRIVER",
    "-DDATA_IN_D2_SRAM",
]

CPP_WARNINGS = [
    "-Wno-register"
]

CPPFLAGS = [
     "-fno-exceptions", 
     "-fno-rtti"
]

C_STANDARD = ["-std=gnu11"]
CPP_STANDARD = ["-std=gnu++11"]

env.Append(CFLAGS = C_STANDARD + C_DEFS)
env.Append(CXXFLAGS = CPP_STANDARD + CPPFLAGS + CPP_WARNINGS)

# linker flags
env.Append(
  LINKFLAGS=[
      "-mfloat-abi=hard",
      "-mfpu=fpv5-sp-d16",
      "--specs=nano.specs",
      "--specs=nosys.specs",
      "-Wl,--gc-sections"
  ]
)
