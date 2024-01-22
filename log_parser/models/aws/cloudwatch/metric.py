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
            "RequestCount": {"Dimensions": ["Resource"]},
            "HealthyStateRouting": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
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
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "RequestCountPerTarget": {"Dimensions": ["TargetGroup"]},
            "HTTPCode_Target_3XX_Count": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "HealthyStateDNS": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "AnomalousHostCount": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "TargetResponseTime": {"Dimensions": ["TargetGroup", "LoadBalancer"]},
            "ClientTLSNegotiationErrorCount": {"Dimensions": ["LoadBalancer"]},
            "ActiveConnectionCount": {"Dimensions": ["LoadBalancer"]},
            "HTTPCode_Target_4XX_Count": {"Dimensions": ["LoadBalancer"]},
            "UnHealthyHostCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "ProcessedBytes": {"Dimensions": ["AvailabilityZone", "LoadBalancer"]},
            "DesyncMitigationMode_NonCompliant_Request_Count": {
                "Dimensions": ["LoadBalancer"]
            },
            "HTTPCode_ELB_503_Count": {"Dimensions": ["LoadBalancer"]},
            "UnhealthyRoutingRequestCount": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "MitigatedHostCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "HTTPCode_ELB_5XX_Count": {"Dimensions": ["LoadBalancer"]},
            "HealthyHostCount": {
                "Dimensions": ["TargetGroup", "AvailabilityZone", "LoadBalancer"]
            },
            "ConsumedLCUs": {"Dimensions": ["LoadBalancer"]},
            "HTTPCode_ELB_3XX_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "RuleEvaluations": {"Dimensions": ["LoadBalancer"]},
            "HTTPCode_Target_5XX_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "ForwardedInvalidHeaderRequestCount": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
            "HTTP_Fixed_Response_Count": {
                "Dimensions": ["AvailabilityZone", "LoadBalancer"]
            },
        },
        "AWS/Lambda": {"Errors": {"Dimensions": ["FunctionName", "Resource"]}},
        "AWS/ECS": {
            "MemoryUtilization": {"Dimensions": ["ServiceName", "ClusterName"]},
            "CPUUtilization": {"Dimensions": ["ServiceName", "ClusterName"]},
        },
        "AWS/RDS": {
            "DDLThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_below_min_rows": {
                "Dimensions": ["DatabaseClass"]
            },
            "VolumeReadIOPs": {"Dimensions": ["EngineName"]},
            "Aurora_pq_request_not_chosen_unsupported_storage_type": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_no_where_clause": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "StorageNetworkThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "InsertLatency": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_throttled": {"Dimensions": ["DBInstanceIdentifier"]},
            "NetworkThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "AuroraBinlogReplicaLag": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_long_trx": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_column_geometry": {
                "Dimensions": ["DatabaseClass"]
            },
            "FreeableMemory": {"Dimensions": ["DBInstanceIdentifier"]},
            "RowLockTime": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ForwardingWriterOpenSessions": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "ForwardingReplicaSelectLatency": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_not_chosen": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "ForwardingWriterDMLLatency": {"Dimensions": ["DatabaseClass"]},
            "BlockedTransactions": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_full_text_index": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "NumBinaryLogFiles": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ForwardingReplicaOpenSessions": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_not_chosen_temporary_table": {
                "Dimensions": ["DatabaseClass"]
            },
            "ReadLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_column_virtual": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "NetworkReceiveThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "DMLLatency": {"Dimensions": ["DBInstanceIdentifier"]},
            "DDLLatency": {"Dimensions": []},
            "CommitThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ForwardingReplicaDMLLatency": {"Dimensions": ["DatabaseClass"]},
            "ConnectionAttempts": {"Dimensions": ["DBInstanceIdentifier"]},
            "EBSByteBalance%": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_failed": {"Dimensions": ["DBClusterIdentifier"]},
            "EBSIOBalance%": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "ForwardingReplicaSelectThroughput": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_innodb_table_format": {
                "Dimensions": ["DBClusterIdentifier"]
            },
            "Queries": {"Dimensions": ["DBClusterIdentifier"]},
            "NetworkTransmitThroughput": {"Dimensions": ["DatabaseClass"]},
            "ActiveTransactions": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_small_table": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "AbortedClients": {"Dimensions": ["DBClusterIdentifier"]},
            "ForwardingWriterDMLThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "ForwardingReplicaReadWaitThroughput": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "DatabaseConnections": {"Dimensions": ["DBInstanceIdentifier"]},
            "Aurora_pq_request_not_chosen_range_scan": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "ForwardingReplicaDMLThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_attempted": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_custom_charset": {"Dimensions": []},
            "InsertThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "SwapUsage": {"Dimensions": []},
            "WriteIOPS": {"Dimensions": ["DBClusterIdentifier"]},
            "CPUUtilization": {"Dimensions": ["DBInstanceIdentifier"]},
            "AuroraSlowConnectionHandleCount": {"Dimensions": ["DBInstanceIdentifier"]},
            "DeleteLatency": {"Dimensions": ["DBInstanceIdentifier"]},
            "UpdateLatency": {"Dimensions": ["DBInstanceIdentifier"]},
            "DMLThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "AuroraDMLRejectedWriterFull": {"Dimensions": ["DBInstanceIdentifier"]},
            "SelectLatency": {"Dimensions": ["DBInstanceIdentifier"]},
            "WriteThroughput": {"Dimensions": ["DatabaseClass"]},
            "UpdateThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "VolumeBytesUsed": {"Dimensions": ["DbClusterIdentifier", "EngineName"]},
            "WriteLatency": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_column_bit": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "DiskQueueDepth": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_row_length_too_long": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_tx_isolation": {"Dimensions": ["EngineName"]},
            "Aurora_pq_request_not_chosen_few_pages_outside_buffer_pool": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_unsupported_access": {
                "Dimensions": ["DBClusterIdentifier"]
            },
            "TotalBackupStorageBilled": {"Dimensions": ["DBClusterIdentifier"]},
            "FreeLocalStorage": {"Dimensions": ["DBInstanceIdentifier"]},
            "SumBinaryLogSize": {"Dimensions": ["DBInstanceIdentifier"]},
            "CPUCreditBalance": {"Dimensions": ["EngineName"]},
            "Aurora_pq_request_not_chosen_column_lob": {
                "Dimensions": ["DBClusterIdentifier"]
            },
            "BufferCacheHitRatio": {"Dimensions": ["DBClusterIdentifier"]},
            "RollbackSegmentHistoryListLength": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_executed": {"Dimensions": ["DBClusterIdentifier"]},
            "LoginFailures": {"Dimensions": ["DBInstanceIdentifier"]},
            "VolumeWriteIOPs": {"Dimensions": ["DbClusterIdentifier", "EngineName"]},
            "SelectThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "AuroraVolumeBytesLeftTotal": {"Dimensions": ["DBInstanceIdentifier"]},
            "ForwardingReplicaReadWaitLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "Deadlocks": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "BackupRetentionPeriodStorageUsed": {"Dimensions": ["EngineName"]},
            "StorageNetworkTransmitThroughput": {"Dimensions": ["DBClusterIdentifier"]},
            "AuroraEstimatedSharedMemoryBytes": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "Aurora_pq_request_not_chosen_high_buffer_pool_pct": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "CPUCreditUsage": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "StorageNetworkReceiveThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "DeleteThroughput": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "AuroraSlowHandshakeCount": {"Dimensions": ["DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_update_delete_stmts": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_in_progress": {
                "Dimensions": ["Role", "DBClusterIdentifier"]
            },
            "CommitLatency": {"Dimensions": ["DBClusterIdentifier"]},
            "ReadIOPS": {"Dimensions": ["Role", "DBClusterIdentifier"]},
            "Aurora_pq_request_not_chosen_index_hint": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "Aurora_pq_request_not_chosen_instant_ddl": {
                "Dimensions": ["DBInstanceIdentifier"]
            },
            "CPUSurplusCreditsCharged": {"Dimensions": []},
            "EngineUptime": {"Dimensions": ["EngineName"]},
            "ReadThroughput": {"Dimensions": ["DBInstanceIdentifier"]},
            "SnapshotStorageUsed": {"Dimensions": ["DBClusterIdentifier"]},
            "CPUSurplusCreditBalance": {"Dimensions": ["Role", "DBClusterIdentifier"]},
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
