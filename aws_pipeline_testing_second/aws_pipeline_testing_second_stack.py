import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_pipeline_testing_second.app_stage import MyPipelineAppStage
from aws_cdk.pipelines import ManualApprovalStep

class AwsPipelineTestingSecondStack(cdk.Stack):

     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("AyushVdoit/aws-pipeline-testing-second", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )
        
        testing_stage =  pipeline.add_stage(MyPipelineAppStage(self, "test4",env=cdk.Environment(account='994546969703', region='eu-central-1')))
        testing_stage.add_post(ManualApprovalStep('approval'))

        prod_stage = pipeline.add_stage(MyPipelineAppStage(self, "prod4",env=cdk.Environment(account='994546969703', region='eu-central-1')))

        # prod_stage.add_pre(ManualApprovalStep('approval'))