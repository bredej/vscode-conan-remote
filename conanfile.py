from conans import ConanFile, CMake

class VscodeConanRemoteConan(ConanFile):
    name = "vscode-conan-remote"
    version = "1.0.0"
    description = "Visual Studio Code example using a Conan Docker image"
    author = "Brede Johansen <bredej@gmail.com>"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt"
    requires = "date/2.4.1"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
