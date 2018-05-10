from devices import SimpleDevice, PatchedDevice, ComplexDevice


# This device has default SSH client
print('--- Simple device example ---')
with SimpleDevice('simple_device') as simple_device:
    simple_device.set_up_ssh()
    simple_device.get_system_info()
    simple_device.get_disk_space()

# This device has a custom SSH client
print('--- Patched simple device example ---')
with PatchedDevice('patched_device') as patched_device:
    patched_device.set_up_ssh()
    patched_device.get_system_info()
    patched_device.get_disk_space()

# This device has multiple SSH connections
print('--- Complex device example ---')
system_node = 'sys'
data_node = 'dat'
with ComplexDevice('complex_device', system_node, data_node) as complex_device:
    complex_device.set_up_ssh(system_node)
    complex_device.set_up_ssh(data_node)
    complex_device.get_system_info()
    complex_device.get_disk_space()


# Output:

# --- Simple device example ---
# Created new device: "simple_device"
# Created SSH connection
# Executing "uname -a"
# Got output: "uname -a" execution output
# Executing "df"
# Got output: "df" execution output
# Stopped SSH connection

# --- Patched simple device example ---
# Created new device: "patched_device"
# Running "uname -a"
# Got output: "uname -a" output
# Running "df"
# Got output: "df" output
# SSH disconnected

# --- Complex device example ---
# Created new device: "complex_device"
# Created SSH connection
# Executing "uname -a"
# Got output: "uname -a" execution output
# Created SSH connection
# Executing "df"
# Got output: "df" execution output
# Stopped SSH connection
# Stopped SSH connection
