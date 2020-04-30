Docker build automation
=======================

Overview
--------

This package provides a script which builds multiple Docker containers in
sequence, using the contents of a ``docker_images.txt`` file in some directory.
This file is tab-delimited, and lines starting with ``#`` are ignored.

Each non-comment line in ``docker_images.txt`` is of the format::

  label    path_to_Dockerfile

(with a tab character between the label and the Dockerfile path, not the
spaces above). Docker images will be built in sequence, so images can refer to
the results of previous images, e.g.::

  image-base    base/Dockerfile
  image-dev     dev/Dockerfile

with ``dev/Dockerfile`` containing::

  FROM image-base
  ...

The container build script checks for any uninitialized Git submodules, and
by default refuses to build if any are found. This can be overridden if
desired (see below).

Usage
-----

The command-line entry point provided by this script is
``build_docker_containers``. By default, images will be tagged with
``:latest`` appended to the base image name.

Options:

--tag-timestamp  In addition to tagging images as ``latest``, also tag with a
                 timestamp in ``YYYYMMDD-HHmmss`` format. All images in
                 ``docker_images.txt`` are tagged with the same timestamp.

--push          Push all built containers to Docker Hub, both with ``latest``
                tags and timestamp tags if ``--tag-timestamp`` is given.

--ignore-missing-submodules  Allow building Docker containers if
                ``git submodule`` reports that at least one submodule is
                uninitialized.

--pretend       Run in pretend mode: don't actually execute anything
                (building, tagging, pushing).

Requirements
------------

Python 3.6 or newer for this script. Docker to build/tag/push images (version
unimportant).
