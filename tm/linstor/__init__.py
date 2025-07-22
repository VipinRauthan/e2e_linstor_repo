IMAGE_PREFIX = "one-image"
SNAP_PREFIX = "snapshot"
VM_NAME_FORMAT = "one-vm-{vm_id}-disk-{disk_id}"
import re

def get_resource_name(src_path):
    match = re.search(r'by-res/([^/]+)/', src_path)
    if match:
        src_path = match.group(1)
    return src_path