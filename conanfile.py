from conans import ConanFile, CMake

class libC(ConanFile):
    name = "libC"
    version = "1.0"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    generators = "cmake"

    scm = {"type": "git",
           "url": "https://github.com/conan-ci-cd-training/libC.git",
           "revision": "auto"}

    def requirements(self):
        self.requires("libA/1.0@mycompany/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = ["libC",]

