from setuptools import find_packages, setup

package_name = 'demo_publisher'

setup(
 name=package_name,
 version='0.0.1',
 packages=find_packages(exclude=['test']),
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
   ],
 install_requires=['setuptools'],
 zip_safe=True,
 maintainer='Cleo Kent',
 maintainer_email='user@todo.todo',
 description='Demo ROS2 Jazzy publisher',
 license='MIT',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'demo_publisher = demo_publisher.main:main'
     ],
   },
)