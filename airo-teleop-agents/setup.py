import setuptools

setuptools.setup(
    name="airo_teleop_agents",
    version="2025.12.0",
    description="Teleop agents that use teleoperation devices from airo_teleop_devices to control specific robot hardware at IDLab-AIRO",
    author="Remko Proesmans",
    author_email="remko.proesmans@ugent.be",
    install_requires=["numpy>=2.0"],
    packages=setuptools.find_packages(exclude=["test"]),
    package_data={"airo_teleop_agents": ["py.typed"]},
)