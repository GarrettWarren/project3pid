from student_pid_class import PID
from pid_controller import PIDController
import yaml
import sys

class StudentPIDController(PIDController):

    def __init__(self):
        super(StudentPIDController, self).__init__()
        with open("z_pid.yaml", "r") as stream:
            try:
                yaml_data = yaml.safe_load(stream)
                kp, ki, kd, k = yaml_data['Kp'], yaml_data['Ki'], yaml_data['Kd'], yaml_data['K']
            except yaml.YAMLError as exc:
                print exc
                print 'Failed to load PID terms! Exiting.'
                sys.exit(1)
        self.pid.throttle = PID(kp, ki, kd, k)


if __name__ == '__main__':
    student_pid_controller = StudentPIDController()
    student_pid_controller.main(StudentPIDController)
