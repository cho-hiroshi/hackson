# Phabricator-on-App-Engine Docker Image

This repo defines a Docker Image that can be used to run Phabricator on App Engine Managed VMs.

## Getting started

### Getting the code

Since Phabricator and its dependencies are fetched as git submodules, you have to include them
when checking out the code:

    git clone --recurse-submodules https://github.com/google/appengine-phabricator
    cd appengine-phabricator

### Installing

The source code includes a script named "install.sh", which deploys the image to a Managed VM.
Assuming that you have your GCP project's name stored in the environment variable "PROJECT", run
the following:

    ./install.sh ${PROJECT}

## Phabricator version

The image is built using a fixed version of the source code for Phabricator and its
dependencies (libphutil and arcanist). These versions are defined by the git submodules
under the "third_party" directory named "arcanist", "libphutil", and "phabricator".

## Included extras

### Backups

This image automatically backs up the contents of the /var/repo directory to the project's default
Google Cloud Storage bucket. Backups are performed every 60 seconds, and on startup the image
automatically tries to restore from the most recent backup (if one exists).

Note that this means you will be billed by GCS for the storage of this backup. To help minimize
this, the image automatically deletes the previous backup after generating a new one.

<!-- TODO(ojarjur): Add a way to disable backups for users who don't want to use hosted repos. -->

### Git/Phabricator mirror

This image includes a daemon which
[mirrors code reviews to and from git-notes](https://github.com/google/git-phabricator-mirror).

That allows the Phabricator instance to integrate with the
[git-appraise command line tool](https://github.com/google/git-appraise), and
makes the use of the arcanist command line tool optional.

Operations performed by the mirror daemon show up as the "git-mirror" bot, which is automatically
created.

### Git authentication

This image includes a git credential helper that automatically authenticates access to
[Google Cloud Repositories](https://cloud.google.com/tools/repo/cloud-repositories) using
the service account of the VM (hence the requirement for the projecthosting scope).

## Development

### Prerequisites

The built image requires an external MySQL instance, and must be run inside of a GCE VM with
the "https://www.googleapis.com/auth/projecthosting" service account scope.

There are four environment variables that must be passed to a Docker container running the image:

1.  "SQL_HOST": The IPv4 address of the MySQL instance
2.  "SQL_PASS": The root password for the MySQL instance
3.  "PHABRICATOR_BASE_URI": The URL of the Phabricator instance (for linking back to itself)
4.  "ALTERNATE_FILE_DOMAIN": A second URL for the Phabricator instance used for linking to untrusted user content

### Building a dev image to test your changes

The image is built using Make. The default target builds a new Docker image and
tags it with the name "google/phabricator-appengine":

    make

You can deploy this locally-built image to a test project using the "deploy" target:

    make deploy PROJECT=${PROJECT}

### Building a testing or stable image

*Note that these two rules require permissions that are restricted to the core developer team.*

The makefile also defines rules for creating a shared testing image, and uploading it to gcr.io.:

    make testing

... and one for labelling the current "testing" image as "latest" (which denotes our stable image):

    make release

### Updating the Phabricator version

This step should be taken with care.

The git-phabricator-mirror tool included in this image calls into the conduit APIs provided by
Phabricator. As such, any breaking changes to those APIs need to be preceded by corresponding
updates to the mirror's use of those APIs.

    git submodule foreach 'cd .. && git submodule update --remote ./'

This will result in pending changes that have to be committed (and pushed) which update the
fixed versions for those submodules.
