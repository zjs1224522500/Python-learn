#!/usr/bin/env python
import sys, rados, rbd

pool_name = "pool"
rbd_size = 1 * 1024 ** 3
rbd_name = "rbd-test"


def create_rbd():

    # Get the cluster info and open cluster
    cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
    cluster.connect()

    # Open the data pool
    ioctx = cluster.open_ioctx(pool_name)

    # Get the RBD management instance and create RBD.
    rbd_inst = rbd.RBD()
    rbd_inst.create(ioctx, rbd_name, rbd_size)
    image = rbd.Image(ioctx, rbd_name)

    # Write date to rbd image eg. foofoofoo...
    data = 'foo' * 200
    # write data with offset. write(data, offset)
    image.write(data, 0)

    # Close the image, context and cluster
    image.close()
    ioctx.close()
    cluster.shutdown()


if __name__ == "__main__":
    create_rbd()