import setuptools

setuptools.setup(
    name="airo_teleop_devices",
    version="2025.12.0",
    description="Drivers for teleoperation devices used in the AIRO teleop framework",
    author="Remko Proesmans",
    author_email="remko.proesmans@ugent.be",
    install_requires=["numpy>=2.0"],
    packages=setuptools.find_packages(exclude=["test"]),
    package_data={"airo_teleop_devices": ["py.typed"]},
)