from setuptools import find_packages, setup

package_name = 'arduinobot_py_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sksuser',
    maintainer_email='sksuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            
            'simple_parameter = arduinobot_py_example.simple_parameter:main',
            'simple_subscriber = arduinobot_py_example.simple_subscriber:main',
            'simple_publisher = arduinobot_py_example.simple_publisher:main',
            'simple_service_server = arduinobot_py_example.simple_service_server:main',
            'simple_service_client = arduinobot_py_example.simple_service_client:main',
            'simple_action_server = arduinobot_py_example.simple_action_server:main',
            'simple_action_client = arduinobot_py_example.simple_action_client:main',
        ],
    },
)
