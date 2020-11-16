Docker build automation
=======================

Overview
--------

This package provides a script which builds multiple Docker containers in
sequence, using the contents of a ``docker_images.txt`` file in some directory.
This file is tab-delimited, and lines starting with ``#`` are ignored.

Each non-comment line in ``docker_images.txt`` is of the format::

  label    path/to/Dockerfile    comma,separated,options,if,desired

(with arbitrary whitespace between pieces). By default, images
will be built by running ``docker build -t label -f Dockerfile .`` in the parent
directory of the Dockerfile. Add the option ``base_directory_build`` after the
Dockerfile to specify that the image should be built with::

  docker build -t label -f path/to/Dockerfile .

in the directory containing ``docker_images.txt`` instead. If the default behavior
is acceptable, the third tab-delimited piece of each line can be omitted.

Docker images will be built in sequence, so images can refer to the results of
previous images, e.g.::

  image-base    base/Dockerfile
  image-dev     dev/Dockerfile

with ``dev/Dockerfile`` containing::

  FROM image-base
  ...

Since images are unconditionally built with the ``latest`` tag, first, then
tagged with a timestamp if desired, no ``Dockerfile`` needs to be modified for
a "release" image.

The container build script checks for any uninitialized Git submodules, and
by default refuses to build if any are found. This can be overridden if
desired (see below).

The build option ``write_git_version`` accepts a file path argument, to which
the output of ``git describe --dirty --always --abbrev=12`` is written. For example::

  image_label    path/to/Dockerfile    write_git_version=src/revision.txt

Usage
-----

The command-line entry point provided by this script is
``build_docker_images``. By default, images will be tagged with
``:latest`` appended to the base image name.

Options:

--tag-timestamp  In addition to tagging images as ``latest``, also tag with a
                 timestamp in ``YYYYMMDD-HHmmss`` format. All images in
                 ``docker_images.txt`` are tagged with the same timestamp.
                 Can be combined with ``--tag=tag_name``.

--tag=tag_name   In addition to tagging images as ``latest``, also tag with the
                 tag name provided. All images in ``docker_images.txt`` are
                 tagged with the same tag name. Can be combined with
                 ``--tag-timestamp``.

--push          Push all built containers to Docker Hub, tagged as ``latest``
                and with any additional tags specified via ``--tag-timestamp``
                or ``--tag=tag_name``.

--ignore-missing-submodules  Allow building Docker containers if
                ``git submodule`` reports that at least one submodule is
                uninitialized.

--pretend       Run in pretend mode: don't actually execute anything
                (building, tagging, pushing).

Requirements
------------

Python 3.6 or newer for this script. Docker to build/tag/push images (version
unimportant).
