from collections import Counter
from typing import Dict


class Metric:
    # {
    #     "NAMESPACE": {
    #         "METRICNAME" : {
    #             "Dimensions": ["", ""]
    #         }
    #     },
    # }
    METRICS: Dict[str, Dict[str, Dict[str, list[str]]]] = {
        "AWS/EC2": {"CPUUtilization": {"Dimensions": ["InstanceId"]}},
        "AWS/ApplicationELB": {
            "RequestCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "HealthyStateRouting": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "UnhealthyStateRouting": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "HTTPCode_ELB_4XX_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "UnhealthyStateDNS": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "NewConnectionCount": {"Dimensions": ["AvailabilityZone", "LoadBalancer"]},
            "HTTPCode_Target_2XX_Count": {
                "Dimensions": ["TargetGroup", "LoadBalancer"]
            },
            "RequestCountPerTarget": {
                "Dimensions": ["TargetGroup", "AvailabilityZone"]
            },
            "HTTPCode_Target_3XX_Count": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "HealthyStateDNS": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "AnomalousHostCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "TargetResponseTime": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "ClientTLSNegotiationErrorCount": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "ActiveConnectionCount": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "HTTPCode_Target_4XX_Count": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "UnHealthyHostCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "ProcessedBytes": {"Dimensions": ["LoadBalancer"]},
            "DesyncMitigationMode_NonCompliant_Request_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "HTTPCode_ELB_503_Count": {"Dimensions": ["LoadBalancer"]},
            "UnhealthyRoutingRequestCount": {
                "Dimensions": ["TargetGroup", "LoadBalancer"]
            },
            "MitigatedHostCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "HTTPCode_ELB_5XX_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "HealthyHostCount": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "ConsumedLCUs": {"Dimensions": ["LoadBalancer"]},
            "HTTPCode_ELB_3XX_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "RuleEvaluations": {"Dimensions": ["LoadBalancer"]},
            "HTTPCode_Target_5XX_Count": {"Dimensions": ["LoadBalancer"]},
            "ForwardedInvalidHeaderRequestCount": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "HTTP_Fixed_Response_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "HTTPCode_ELB_504_Count": {"Dimensions": ["LoadBalancer"]},
        },
        "AWS/Lambda": {"Errors": {"Dimensions": ["FunctionName", "Resource"]}},
        "AWS/ECS": {
            "MemoryUtilization": {"Dimensions": ["ServiceName", "ClusterName"]},
            "CPUUtilization": {"Dimensions": ["ServiceName", "ClusterName"]},
        },
        "AWS/RDS": {
            "DDLThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_below_min_rows": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "VolumeReadIOPs": {"Dimensions": ["DbClusterIdentifier", "EngineName"]},
            "Aurora_pq_request_not_chosen_unsupported_storage_type": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_no_where_clause": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "StorageNetworkThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "InsertLatency": {"Dimensions": []},
            "Aurora_pq_request_throttled": {"Dimensions": ["DBInstanceIdentifier"]},
            "NetworkThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "AuroraBinlogReplicaLag": {"Dimensions": []},
            "Aurora_pq_request_not_chosen_long_trx": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_column_geometry": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "FreeableMemory": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "RowLockTime": {"Dimensions": ["DBInstanceIdentifier"]},
            "ForwardingWriterOpenSessions": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "ForwardingReplicaSelectLatency": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen": {"Dimensions": ["DBClusterIdentifier"]},
            "ForwardingWriterDMLLatency": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "BlockedTransactions": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_full_text_index": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "NumBinaryLogFiles": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ForwardingReplicaOpenSessions": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_temporary_table": {
                "Dimensions": ["DBClusterIdentifier"]
            },
            "ReadLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_column_virtual": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "NetworkReceiveThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "DMLLatency": {"Dimensions": ["DatabaseClass"]},
            "DDLLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "CommitThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "ForwardingReplicaDMLLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "ConnectionAttempts": {"Dimensions": ["DBClusterIdentifier"]},
            "EBSByteBalance%": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_failed": {"Dimensions": ["DBClusterIdentifier"]},
            "EBSIOBalance%": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ForwardingReplicaSelectThroughput": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_innodb_table_format": {
                "Dimensions": ["DBClusterIdentifier"]
            },
            "Queries": {"Dimensions": ["DBInstanceIdentifier"]},
            "NetworkTransmitThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "ActiveTransactions": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_small_table": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "AbortedClients": {"Dimensions": ["DBInstanceIdentifier"]},
            "ForwardingWriterDMLThroughput": {"Dimensions": []},
            "ForwardingReplicaReadWaitThroughput": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "DatabaseConnections": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_range_scan": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "ForwardingReplicaDMLThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_attempted": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_not_chosen_custom_charset": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "InsertThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "SwapUsage": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "WriteIOPS": {"Dimensions": ["DBInstanceIdentifier"]},
            "CPUUtilization": {"Dimensions": ["DBClusterIdentifier"]},
            "AuroraSlowConnectionHandleCount": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "DeleteLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "UpdateLatency": {"Dimensions": ["EngineName"]},
            "DMLThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "AuroraDMLRejectedWriterFull": {"Dimensions": ["DBClusterIdentifier"]},
            "SelectLatency": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "WriteThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "UpdateThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "VolumeBytesUsed": {"Dimensions": ["DbClusterIdentifier", "EngineName"]},
            "WriteLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_column_bit": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "DiskQueueDepth": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_not_chosen_row_length_too_long": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_tx_isolation": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_few_pages_outside_buffer_pool": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_unsupported_access": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "TotalBackupStorageBilled": {"Dimensions": ["DBClusterIdentifier"]},
            "FreeLocalStorage": {"Dimensions": ["DBInstanceIdentifier"]},
            "SumBinaryLogSize": {"Dimensions": ["DBClusterIdentifier"]},
            "CPUCreditBalance": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_column_lob": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "BufferCacheHitRatio": {"Dimensions": ["DBInstanceIdentifier"]},
            "RollbackSegmentHistoryListLength": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_executed": {"Dimensions": ["DBClusterIdentifier"]},
            "LoginFailures": {"Dimensions": ["DBInstanceIdentifier"]},
            "VolumeWriteIOPs": {"Dimensions": ["DBClusterIdentifier"]},
            "SelectThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "AuroraVolumeBytesLeftTotal": {"Dimensions": ["DBInstanceIdentifier"]},
            "ForwardingReplicaReadWaitLatency": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Deadlocks": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "BackupRetentionPeriodStorageUsed": {"Dimensions": ["DBClusterIdentifier"]},
            "StorageNetworkTransmitThroughput": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "AuroraEstimatedSharedMemoryBytes": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_high_buffer_pool_pct": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "CPUCreditUsage": {"Dimensions": ["DBClusterIdentifier"]},
            "StorageNetworkReceiveThroughput": {"Dimensions": []},
            "DeleteThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "AuroraSlowHandshakeCount": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_update_delete_stmts": {
                "Dimensions": ["DBClusterIdentifier"]
            },
            "Aurora_pq_request_in_progress": {"Dimensions": ["DBInstanceIdentifier"]},
            "CommitLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "ReadIOPS": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_not_chosen_index_hint": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_instant_ddl": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "CPUSurplusCreditsCharged": {"Dimensions": ["DBClusterIdentifier"]},
            "EngineUptime": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ReadThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "SnapshotStorageUsed": {"Dimensions": ["DBClusterIdentifier"]},
            "CPUSurplusCreditBalance": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "AuroraReplicaLag": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "AuroraReplicaLagMinimum": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "AuroraReplicaLagMaximum": {"Dimensions": ["DBClusterIdentifier"]},
        },
    }

    STATS: list[str] = []

    @classmethod
    def check_namespace(cls, namespace: str) -> bool:
        return namespace in cls.METRICS

    @classmethod
    def check_metric_name(cls, namespace: str, metric_name: str) -> bool:
        return metric_name in cls.METRICS[namespace]

    @classmethod
    def check_dimensions(
        cls, namespace: str, metric_name: str, dimensions: list[str]
    ) -> bool:
        return Counter(cls.METRICS[namespace][metric_name]["Dimensions"]) == Counter(
            dimensions
        )
