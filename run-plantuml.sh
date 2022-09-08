#!/usr/bin/env bash

__run_plantuml() {
    local docker_image="miy4/plantuml"
    local host_src_volume="${PWD}"
    local container_dest_volume="/work"

    exec docker run --volume="${host_src_volume}:${container_dest_volume}" --workdir="${container_dest_volume}" --rm --attach=stdin --attach=stdout --attach=stderr --interactive "${docker_image}" "$@"
}

__run_plantuml "$@"
