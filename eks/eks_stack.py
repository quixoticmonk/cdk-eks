from aws_cdk import (core as cdk, aws_eks as _eks, aws_ec2 as _ec2, aws_kms as
                     _kms)


class EksStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _secrets_key = _kms.Key(
            self,
            "clusterkey",
            enabled=True,
            enable_key_rotation=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            description="Key created for envelope encryption")

        _cluster = _eks.Cluster(
            self,
            "cluster",
            cluster_name="eks-cluster",
            version=_eks.KubernetesVersion.V1_19,
            default_capacity=5,
            default_capacity_instance=_ec2.InstanceType.of(
                _ec2.InstanceClass.MEMORY5, _ec2.InstanceSize.LARGE),
            output_cluster_name=True,
            output_config_command=True,
            secrets_encryption_key=_secrets_key
        )
