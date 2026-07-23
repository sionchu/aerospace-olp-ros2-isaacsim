from setuptools import find_packages, setup

package_name = "aerospace_olp_bringup"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Jeongeon Lee",
    maintainer_email="jeongeonlee92@gmail.com",
    description="ROS 2 command and monitoring utilities for the Isaac Sim aerospace OLP project.",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "aero_drill_terminal = aerospace_olp_bringup.aero_drill_terminal:main",
        ],
    },
)
