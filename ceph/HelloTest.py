#!/usr/bin/python
# encoding=utf-8
import rados
import sys

try:
    cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
except TypeError as e:
    print('Argument validation error: ', e)
    raise e
print("Created cluster handle.")

try:
    cluster.connect()
except Exception as e:
    print("connection error: ", e)
    raise e
finally:
    print("Connected to the cluster.")

pool_name = "data-test-shunzi"

print("\n\nI/O Context and Object Operations")
print("=================================")
print("\nCreating a context for the '%s' pool" % pool_name)

# List pool names
pools = cluster.list_pools()
print("\nList pools in ceph:")
for pool in pools:
    print(" " + pool)

# Create the pool with the pool name
print("\nCreate the data pool with pool name '%s'." % pool_name)
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
print("\nWriting XATTR 'lang' with value 'fr_FR' to object 'name'")
ioctx.set_xattr("name", "lang", "fr_FR")


# Reading object data
print("\nContents of object 'school'\n------------------------")
print(ioctx.read("school"))
# Reading XATTR data (objectKey, attributeKey)
print(ioctx.get_xattr("name", "lang"))

# Reading object data
print("\nContents of object 'name'\n------------------------")
print(ioctx.read("name"))

# Append object data
print("\n Append object 'name'\n-----------------------------")
ioctx.append('name', 'append value~~~')
print("\n Contents of object 'name'\n------------------------")
print(ioctx.read("name"))

# Remove object data
print("\n Remove object 'school'\n---------------------------")
ioctx.remove_object("school")
print("\n Contents of object 'school'\n------------------------")
print(ioctx.read("school"))


# Close the io context and delete the pool created temporarily
print("\n Closing the connection.")
ioctx.close()
cluster.delete_pool(pool_name)

print("\n Shutting down the handle.")
cluster.shutdown()

