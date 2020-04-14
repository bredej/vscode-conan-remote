# Cross build and debug conan packages using docker and vscode

The title says it all.

Before bringing vscode into the mix make sure you understand how to [create conan packages using docker](https://docs.conan.io/en/1.10/howtos/run_conan_in_docker.html)  

This example is based on [this repo](https://github.com/Microsoft/vscode-remote-try-cpp) and modified to work with conan.
There are tasks in vscode for 
    - conan install
    - conan build
