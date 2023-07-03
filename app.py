#!/usr/bin/env python3
import aws_cdk as cdk
from aws_pipeline_testing_second.aws_pipeline_testing_second_stack import AwsPipelineTestingSecondStack

app = cdk.App()
AwsPipelineTestingSecondStack(app, "AwsPipelineTestingSecondStack",
    env=cdk.Environment(account='994546969703', region='eu-central-1')
)

app.synth()
