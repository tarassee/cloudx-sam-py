prerequisites:
- CodeBuild
- CodePipeline

to consider:
- add proper IAM policies for CodeBuild, CodePipeline, Lambda
- CF duplicates arn of SNS Lambda Resource policy, so fix it manually

todo: 
- configure `[skip ci]` in commit message to skip pipeline triggering

CodePipeline view:
![img.png](doc/img.png)
