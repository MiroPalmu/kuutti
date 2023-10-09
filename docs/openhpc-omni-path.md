# Omni-Path support

Omni-Path requires following package: `opa-basic-tools`

From OpenHPC manual:

> Omni-Path networks require a subnet management service that can typically be run on either an administrative node, or on the switch itself. The optimal placement and configuration of the subnet manager is beyond the scope of this document, but Rocky 8.6 provides the opa-fm package should you choose to run it on the master node.

# Omni-Path library

`libpsm2`

# Increase locked memory limits

From OpenHPC Manual:

> In order to utilize InfiniBand or Omni-Path as the underlying high speed interconnect, it is generally necessary to increase the locked memory settings for system users. This can be accomplished by updating the /etc/security/limits.conf file and this should be performed within the compute image and on all job submission hosts. In this recipe, jobs are submitted from the master host, and the following commands can be used to update the maximum locked memory settings on both the master host and the compute image

```
# Update memlock settings on master
[sms]# perl -pi -e 's/# End of file/\* soft memlock unlimited\n$&/s' /etc/security/limits.conf
[sms]# perl -pi -e 's/# End of file/\* hard memlock unlimited\n$&/s' /etc/security/limits.conf
# Update memlock settings within compute image
[sms]# perl -pi -e 's/# End of file/\* soft memlock unlimited\n$&/s' $CHROOT/etc/security/limits.conf
[sms]# perl -pi -e 's/# End of file/\* hard memlock unlimited\n$&/s' $CHROOT/etc/security/limits.conf
```

# MPI Stacks

From OpenHPC manual, the available MPI stacks:

|                   | Ethernet (TCP) | InfiniBand | Intel(R) Omni-Path |
|-------------------|----------------|------------|--------------------|
| MPICH(ofi)        | x              | x          | x                  |
| MPICH (ucx)       | x              | x          | x                  |
| MVAPICH2          |                | x          |                    |
| MVAPICH2 (psm2)   |                |            | x                  |
| OpenMPI (ofi/ucx) | x              | x          | x                  |

So if one chooses MVAPICH2 has to be installed with psm2 support with package `mvapich2-psm2-gnu12-ohpc`

# Default development enviroment

OpenHPC provides different default enviroments:

- `lmod-defaults-gnu12-openmpi4-ohpc`
- `lmod-defaults-gnu12-mpich-ofi-ohpc`
- `lmod-defaults-gnu12-mpich-ucx-ohpc`
- `lmod-defaults-gnu12-mvapich2-ohpc`

# Intel OneAPI Omni-Path

Intel OneAPI is enable with packages:

```
yum -y install intel-oneapi-toolkit-release-ohpc
rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
yum -y install intel-compilers-devel-ohpc
yum -y install intel-mpi-devel-ohpc
```

There is `mvapich2-psm2-intel-ohpc` package to enable mvpich2 Omni-Path support for Intel compilers.
