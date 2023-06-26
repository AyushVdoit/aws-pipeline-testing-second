import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_pipeline_testing_second.aws_pipeline_testing_second_stack import AwsPipelineTestingSecondStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_pipeline_testing_second/aws_pipeline_testing_second_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsPipelineTestingSecondStack(app, "aws-pipeline-testing-second")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
