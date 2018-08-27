Hat Backup System
=================
Disclaimer: This is not an official Google product.

Warning: This is an incomplete work-in-progress.

Warning: This project does currently NOT support security or privacy.

[![Build Status](https://travis-ci.org/google/hat-backup.svg?branch=master)](https://travis-ci.org/google/hat-backup)

Project
-------
The goal of hat is to provide a backend-agnostic snapshotting backup system,
complete with deduplication of file blocks and efficient navigation of backed up
files.

A sub-goal is to do so in a safe and fault-tolerant manner, where a process
crash is followed by quick and safe recovery.

Further, we aim for readable and maintainable code, partly by splitting the
system into a few sub-systems with clear responsibility.

Disclaimer: The above text describes our goal and not the current status.

Status
------
This software is pre-alpha and should be considered severely unstable.

This software should not be considered ready for any use; the code is currently
provided for development and experimentation purposes only.

Roadmap to a first stable release
---------------------------------
**Cleanup:**

I am currently focusing on reaching a feature complete and useful state and as a result, I am skipping quickly over some implementation details. The following items will have to be revisited and cleaned up before a stable release:

- Properly support non-utf8 paths.
- Store and restore all relevant file metadata
  - same for symlinks.
- ~~Use prepared statements when communicating with SQLite.~~
- ~~Run rustfmt on the code when it is ready.~~
- ~~Reimplement argument handling in main; possibly using docopt.~~ [thanks kbknapp]
- ~~Replace all uses of JSON with either Protocol Buffers or Cap'n Proto.~~
- Go through uses of 'unwrap', 'expect' etc and remove them where possible; preferably, the caller/initiater should handle errors.
- Think about parallelism and change the pipeline of threads to make better use of it.
  - ~~Parallel snapshotting~~
- Figure out how to battle test the code on supported platforms.

**Functionality:**

There are a bunch of lacking functionality needed before a feature complete release is in sight:

- ~~Commit hash-tree tops of known snapshots to external storage.~~
- Add recovery function to restore local metadata from external hash-tree tops (for when all local state is gone).
  - ~~Basic read-only recovery.~~
  - ~~Full read-write recovery with GC metadata rebuilding.~~
  - Need to allow users to opt for read-only.
- ~~Add book-keeping for metadata needed to identify live hashes (e.g. reference sets in each family's keyindex).~~
- ~~Add deletion and garbage-collection.~~
  - ~~Make 'commit' crash-safe by retrying failed 'register' and 'deregister' runs~~. Add tests as this is fragile logic.
  - ~~GC should not be able to break the index. This can be avoided by having 'snapshot' check if hashes it wants to reuse still exist (i.e. have not been GC'ed yet).~~
  - ~~GC should delete hashes top-down to avoid removing a child hash before its parent hash.~~
- Have the blobstore talk to external thread(s) to isolate communication with external storage.
- Make the API used for talking to the external storage easy to change (put it in separate put/get/del programs).
- Add encryption through NaCL/sodiumdioxide; preferably as late as possible.

**Future wishlist: (not blocking first release)**

- Output a dot graph over current hash trees to show dependencies and reuse.
- FSCK style metadata verification ("check" subcommand?).
- Commit snapshots while indexing them (possibly through "weak" snapshots that are ignored by GC). The purpose is to allow checking out a partial snapshot.
- Add "--pretend" to all subcommands and have it give a signal as to what would happen without it.

Building from source
--------------------
First, make sure you have the required system libraries and tools installed:
* libsodium
* libsqlite3
* capnproto (at least version 0.5.3)

0. Install rust (try nightly or check commit log for compatible version)
   * Rust nighly is available from http://rust-lang.org
1. Checkout the newest version of the source:
   * `git clone https://github.com/google/hat-backup.git`
   * `cd hat`
2. Let Cargo build everything needed:
   * `cargo build --release`

Try the hat executable using Cargo (the binary is in target/release/)
---------------------------------------------------------------------
   * `cargo run --release snapshot my_snapshot /some/path/to/dir`
   * `cargo run --release commit my_snapshot`
   * `cargo run --release checkout my_snapshot output/dir`

License and copyright
---------------------
See the files LICENSE and AUTHORS.

Contributions
-------------
We gladly accept contributions/fixes/improvements etc. via GitHub pull requests
or any other reasonable means, as long as the author has signed the Google
Contributor License.

The Contributor License exists in two versions, one for individuals and one for
corporations:

https://developers.google.com/open-source/cla/individual
https://developers.google.com/open-source/cla/corporate


Please read and sign one of the above versions of the Contributor License,
before sending your contribution. Thanks!

Authors
-------
See the AUTHORS.txt file.

This project is inspired by a previous version of the system written in Haskell:
https://github.com/mortenbp/hindsight
