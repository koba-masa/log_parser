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
    METRICS: Dict[str, Dict[str, Dict[str, list[list[str]]]]] = {
        "AWS/Lambda": {"Errors": {"Dimensions": [["FunctionName", "Resource"]]}},
        "AWS/ApplicationELB": {
            "HealthyStateRouting": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "RequestCount": {
                "Dimensions": [
                    ["TargetGroup", "LoadBalancer"],
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["AvailabilityZone", "LoadBalancer"],
                    ["LoadBalancer"],
                ]
            },
            "UnhealthyStateDNS": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "HTTPCode_Target_2XX_Count": {
                "Dimensions": [
                    ["AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["LoadBalancer"],
                ]
            },
            "RequestCountPerTarget": {
                "Dimensions": [
                    ["TargetGroup"],
                    ["TargetGroup", "LoadBalancer"],
                    ["TargetGroup", "AvailabilityZone"],
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                ]
            },
            "TargetResponseTime": {
                "Dimensions": [
                    ["AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["LoadBalancer"],
                ]
            },
            "HTTPCode_Target_3XX_Count": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["LoadBalancer"],
                    ["AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "HealthyStateDNS": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "AnomalousHostCount": {
                "Dimensions": [
                    ["TargetGroup", "LoadBalancer"],
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                ]
            },
            "UnhealthyStateRouting": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "NewConnectionCount": {
                "Dimensions": [["AvailabilityZone", "LoadBalancer"], ["LoadBalancer"]]
            },
            "ActiveConnectionCount": {
                "Dimensions": [["LoadBalancer"], ["AvailabilityZone", "LoadBalancer"]]
            },
            "HTTPCode_Target_4XX_Count": {
                "Dimensions": [
                    ["LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                    ["AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                ]
            },
            "UnHealthyHostCount": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "HTTPCode_ELB_4XX_Count": {
                "Dimensions": [["LoadBalancer"], ["AvailabilityZone", "LoadBalancer"]]
            },
            "DesyncMitigationMode_NonCompliant_Request_Count": {
                "Dimensions": [["LoadBalancer"], ["AvailabilityZone", "LoadBalancer"]]
            },
            "UnhealthyRoutingRequestCount": {
                "Dimensions": [
                    ["AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "MitigatedHostCount": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "ProcessedBytes": {
                "Dimensions": [["LoadBalancer"], ["AvailabilityZone", "LoadBalancer"]]
            },
            "HealthyHostCount": {
                "Dimensions": [
                    ["TargetGroup", "AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                ]
            },
            "HTTPCode_ELB_5XX_Count": {
                "Dimensions": [["AvailabilityZone", "LoadBalancer"], ["LoadBalancer"]]
            },
            "ClientTLSNegotiationErrorCount": {
                "Dimensions": [["AvailabilityZone", "LoadBalancer"], ["LoadBalancer"]]
            },
            "ConsumedLCUs": {"Dimensions": [["LoadBalancer"]]},
            "HTTPCode_ELB_3XX_Count": {
                "Dimensions": [["AvailabilityZone", "LoadBalancer"]]
            },
            "HTTPCode_ELB_504_Count": {"Dimensions": [["LoadBalancer"]]},
            "HTTPCode_Target_5XX_Count": {
                "Dimensions": [
                    ["AvailabilityZone", "LoadBalancer"],
                    ["TargetGroup", "LoadBalancer"],
                    ["LoadBalancer"],
                ]
            },
            "ForwardedInvalidHeaderRequestCount": {
                "Dimensions": [["AvailabilityZone", "LoadBalancer"], ["LoadBalancer"]]
            },
            "RuleEvaluations": {"Dimensions": [["LoadBalancer"]]},
            "HTTP_Fixed_Response_Count": {
                "Dimensions": [["AvailabilityZone", "LoadBalancer"]]
            },
        },
        "AWS/ECS": {
            "CPUUtilization": {"Dimensions": [["ServiceName", "ClusterName"]]},
            "MemoryUtilization": {"Dimensions": [["ServiceName", "ClusterName"]]},
        },
        "AWS/RDS": {
            "AuroraReplicaLag": {"Dimensions": [["Role", "DBClusterIdentifier"]]},
            "VolumeReadIOPs": {
                "Dimensions": [["EngineName"], ["DbClusterIdentifier", "EngineName"]]
            },
            "Aurora_pq_request_not_chosen_unsupported_storage_type": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["DBInstanceIdentifier"],
                ]
            },
            "NumBinaryLogFiles": {"Dimensions": [["Role", "DBClusterIdentifier"]]},
            "ForwardingReplicaSelectLatency": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["EngineName"],
                ]
            },
            "InsertLatency": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DatabaseClass"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    [],
                ]
            },
            "Aurora_pq_request_not_chosen_column_geometry": {
                "Dimensions": [
                    ["DatabaseClass"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    [],
                ]
            },
            "FreeableMemory": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "RowLockTime": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DatabaseClass"],
                ]
            },
            "Aurora_pq_request_throttled": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "ForwardingWriterOpenSessions": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    [],
                    ["EngineName"],
                ]
            },
            "Aurora_pq_request_not_chosen": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "StorageNetworkReceiveThroughput": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    [],
                ]
            },
            "ForwardingWriterDMLLatency": {
                "Dimensions": [
                    ["DatabaseClass"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_full_text_index": {
                "Dimensions": [["Role", "DBClusterIdentifier"]]
            },
            "ForwardingReplicaOpenSessions": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["DBClusterIdentifier"],
                ]
            },
            "ReadLatency": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "NetworkReceiveThroughput": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "DDLLatency": {
                "Dimensions": [
                    [],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "CommitThroughput": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_below_min_rows": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    [],
                ]
            },
            "ForwardingReplicaDMLLatency": {
                "Dimensions": [
                    ["DatabaseClass"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["EngineName"],
                ]
            },
            "ConnectionAttempts": {
                "Dimensions": [["DBInstanceIdentifier"], ["DBClusterIdentifier"], []]
            },
            "EBSByteBalance%": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "AuroraDMLRejectedWriterFull": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "CommitLatency": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_innodb_table_format": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DatabaseClass"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Queries": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DatabaseClass"],
                ]
            },
            "NetworkTransmitThroughput": {
                "Dimensions": [
                    ["DatabaseClass"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "ActiveTransactions": {
                "Dimensions": [["Role", "DBClusterIdentifier"], ["DBClusterIdentifier"]]
            },
            "Aurora_pq_request_not_chosen_small_table": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DatabaseClass"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "AbortedClients": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "ForwardingWriterDMLThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["EngineName"],
                    [],
                ]
            },
            "ForwardingReplicaReadWaitThroughput": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "DatabaseConnections": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["DBClusterIdentifier"],
                ]
            },
            "ForwardingReplicaDMLThroughput": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Aurora_pq_request_attempted": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_custom_charset": {
                "Dimensions": [
                    [],
                    ["Role", "DBClusterIdentifier"],
                    ["EngineName"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_instant_ddl": {
                "Dimensions": [["DBInstanceIdentifier"], ["DBClusterIdentifier"]]
            },
            "BlockedTransactions": {
                "Dimensions": [
                    [],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_long_trx": {
                "Dimensions": [["DBClusterIdentifier"], ["DBInstanceIdentifier"]]
            },
            "SwapUsage": {
                "Dimensions": [[], ["DatabaseClass"], ["Role", "DBClusterIdentifier"]]
            },
            "WriteIOPS": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["EngineName"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "CPUUtilization": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "AuroraSlowConnectionHandleCount": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["EngineName"],
                ]
            },
            "DeleteLatency": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "DDLThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_failed": {
                "Dimensions": [["Role", "DBClusterIdentifier"], ["DBClusterIdentifier"]]
            },
            "DMLThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["EngineName"],
                    ["DBClusterIdentifier"],
                ]
            },
            "AuroraReplicaLagMinimum": {
                "Dimensions": [["Role", "DBClusterIdentifier"]]
            },
            "SelectLatency": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["EngineName"],
                ]
            },
            "UpdateThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "WriteLatency": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_column_bit": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DatabaseClass"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "ForwardingReplicaSelectThroughput": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["DBInstanceIdentifier"],
                ]
            },
            "DiskQueueDepth": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "StorageNetworkThroughput": {
                "Dimensions": [["DBInstanceIdentifier"], ["DBClusterIdentifier"]]
            },
            "AuroraReplicaLagMaximum": {
                "Dimensions": [["Role", "DBClusterIdentifier"], ["DBClusterIdentifier"]]
            },
            "Aurora_pq_request_not_chosen_temporary_table": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_tx_isolation": {
                "Dimensions": [
                    ["EngineName"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "InsertThroughput": {
                "Dimensions": [
                    ["DatabaseClass"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_few_pages_outside_buffer_pool": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_unsupported_access": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    [],
                    ["EngineName"],
                ]
            },
            "CPUCreditBalance": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["EngineName"],
                    ["DBInstanceIdentifier"],
                    [],
                    ["DBClusterIdentifier"],
                ]
            },
            "TotalBackupStorageBilled": {"Dimensions": [["DBClusterIdentifier"]]},
            "FreeLocalStorage": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "NetworkThroughput": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "DMLLatency": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DatabaseClass"],
                ]
            },
            "Aurora_pq_request_not_chosen_column_lob": {
                "Dimensions": [["DBClusterIdentifier"], ["Role", "DBClusterIdentifier"]]
            },
            "AuroraBinlogReplicaLag": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    [],
                ]
            },
            "BufferCacheHitRatio": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "RollbackSegmentHistoryListLength": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DatabaseClass"],
                ]
            },
            "Aurora_pq_request_not_chosen_row_length_too_long": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_executed": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "VolumeWriteIOPs": {
                "Dimensions": [
                    ["DbClusterIdentifier", "EngineName"],
                    ["DBClusterIdentifier"],
                ]
            },
            "AuroraVolumeBytesLeftTotal": {"Dimensions": [["DBInstanceIdentifier"]]},
            "ForwardingReplicaReadWaitLatency": {
                "Dimensions": [["DBClusterIdentifier"], ["DBInstanceIdentifier"]]
            },
            "Deadlocks": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["EngineName"],
                ]
            },
            "BackupRetentionPeriodStorageUsed": {
                "Dimensions": [["EngineName"], ["DBClusterIdentifier"]]
            },
            "LoginFailures": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DatabaseClass"],
                ]
            },
            "StorageNetworkTransmitThroughput": {
                "Dimensions": [["DBClusterIdentifier"], ["DBInstanceIdentifier"]]
            },
            "Aurora_pq_request_not_chosen_high_buffer_pool_pct": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "CPUCreditUsage": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_column_virtual": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    [],
                ]
            },
            "SelectThroughput": {"Dimensions": [["DBInstanceIdentifier"]]},
            "WriteThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "SumBinaryLogSize": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_update_delete_stmts": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DatabaseClass"],
                    ["DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_in_progress": {
                "Dimensions": [
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                ]
            },
            "EBSIOBalance%": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "AuroraEstimatedSharedMemoryBytes": {
                "Dimensions": [["DBClusterIdentifier"], ["DBInstanceIdentifier"]]
            },
            "DeleteThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "AuroraSlowHandshakeCount": {
                "Dimensions": [["Role", "DBClusterIdentifier"], ["DBClusterIdentifier"]]
            },
            "UpdateLatency": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                    ["DBClusterIdentifier"],
                    ["EngineName"],
                ]
            },
            "Aurora_pq_request_not_chosen_index_hint": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DBClusterIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "Aurora_pq_request_not_chosen_range_scan": {
                "Dimensions": [["DBClusterIdentifier"], ["Role", "DBClusterIdentifier"]]
            },
            "CPUSurplusCreditsCharged": {
                "Dimensions": [
                    [],
                    ["Role", "DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["EngineName"],
                    ["DBClusterIdentifier"],
                ]
            },
            "EngineUptime": {
                "Dimensions": [
                    ["EngineName"],
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "ReadIOPS": {
                "Dimensions": [["DBClusterIdentifier"], ["DBInstanceIdentifier"]]
            },
            "ReadThroughput": {
                "Dimensions": [
                    ["DBInstanceIdentifier"],
                    ["DatabaseClass"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "SnapshotStorageUsed": {"Dimensions": [["DBClusterIdentifier"]]},
            "Aurora_pq_request_not_chosen_no_where_clause": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DBInstanceIdentifier"],
                    ["Role", "DBClusterIdentifier"],
                ]
            },
            "VolumeBytesUsed": {
                "Dimensions": [
                    ["DBClusterIdentifier"],
                    ["DbClusterIdentifier", "EngineName"],
                ]
            },
            "CPUSurplusCreditBalance": {
                "Dimensions": [["Role", "DBClusterIdentifier"]]
            },
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
        cls, namespace: str, metric_name: str, dimension_keys: list[str]
    ) -> bool:
        for dimension in cls.METRICS[namespace][metric_name]["Dimensions"]:
            if Counter(dimension) == Counter(dimension_keys):
                return True
        return False
