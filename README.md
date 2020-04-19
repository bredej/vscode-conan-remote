# Cross build and debug conan packages using docker and vscode

With the Visual Studio Code *Remote-Containers* extension it is possible to debug inside a Docker container.  
[Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)

Before bringing vscode into the mix make sure you understand how to [create conan packages using docker](https://docs.conan.io/en/1.10/howtos/run_conan_in_docker.html).  

This example is based on [this repo](https://github.com/Microsoft/vscode-remote-try-cpp) and adapted to work with Docker images provided by [Conan Docker Tools](https://github.com/conan-io/conan-docker-tools).

Tasks are setup to do the **conan install** and **conan build** commands.
