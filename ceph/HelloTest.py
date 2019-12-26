#!/usr/bin/python
# encoding=utf-8
import rados
import sys

cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
cluster.connect()
pool_name = "data-test-shunzi"

print("\n\nI/O Context and Object Operations")
print("=================================")
print("\nCreating a context for the '%s' pool" % pool_name)

pools = cluster.list_pools()
print("\nList pools in ceph:")
for pool in pools:
    print(pool, end=", ")
cluster.create_pool(pool_name)
if not cluster.pool_exists(pool_name):
    raise RuntimeError("No data pool named '%s' exists" % pool_name)

ioctx = cluster.open_ioctx(pool_name)

# Writing Object Data
print("\nWriting object 'school' with contents 'hello , I are from chd university!' to pool 'data'.")
ioctx.write("school", "hello , I are from chd university!")
# Writing XATTR Data (objectKey, attributeKey, attributeValue)
ioctx.set_xattr("school", "lang", "en_US")

# Writing Object Data
print("\nWriting object 'name' with contents 'my name is lxl!' to pool 'data'.")
ioctx.write("name", "my name is lxl!")
# Writing XATTR Data (objectKey, attributeKey, attributeValue)
print("Writing XATTR 'lang' with value 'fr_FR' to object 'name'")
ioctx.set_xattr("name", "lang", "fr_FR")

# Reading object data
print("\nContents of object 'school'\n------------------------")
print(ioctx.read("school"))
# Reading XATTR data (objectKey, attributeKey)
print(ioctx.get_xattr("name", "lang"))

# Reading object data
print("\nContents of object 'name'\n------------------------")
print(ioctx.read("name"))
print("\nClosing the connection.")

# Close the io context and delete the pool created temporarily
ioctx.close()
cluster.delete_pool(pool_name)
