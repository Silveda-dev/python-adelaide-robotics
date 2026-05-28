from setuptools import find_packages, setup

package_name = 'demo_subscriber'

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
 description='Demo ROS2 Jazzy subscriber',
 license='MIT',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'demo_subscriber = demo_subscriber.main:main'
     ],
   },
)