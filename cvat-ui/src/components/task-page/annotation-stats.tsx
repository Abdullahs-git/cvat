import React, { useEffect, useState } from 'react';
import { Row, Col } from 'antd/lib/grid';
import Spin from 'antd/lib/spin';
import Alert from 'antd/lib/alert';
import Text from 'antd/lib/typography/Text';
import Progress from 'antd/lib/progress';
import Empty from 'antd/lib/empty';
import Button from 'antd/lib/button';
import { getCore, Task } from 'cvat-core-wrapper';

const core = getCore();

interface AnnotationStatsProps {
    task: Task;
}

interface ClassCount {
    label_id: number;
    name: string;
    color: string;
    count: number;
}

interface StatsResponse {
    task_id: number;
    total: number;
    classes: ClassCount[];
}

export default function AnnotationStats({ task }: AnnotationStatsProps): JSX.Element {
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [stats, setStats] = useState<StatsResponse | null>(null);

    const fetchStats = async (): Promise<void> => {
        setLoading(true);
        setError(null);
        try {
            const response = await core.server.request(
                /api/annotation-stats/tasks//class-counts,
                { method: 'GET' }
            );
            setStats(response);
        } catch (err: any) {
            setError(err.message || 'Failed to fetch annotation stats');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchStats();
    }, [task.id]);

    if (loading) {
        return (
            <div style={{ textAlign: 'center', padding: '20px' }}>
                <Spin size="default" />
                <Text style={{ marginLeft: '10px' }}>Loading annotation stats...</Text>
            </div>
        );
    }

    if (error) {
        return (
            <Alert
                message="Error"
                description={error}
                type="error"
                showIcon
                action={
                    <Button size="small" danger onClick={fetchStats}>
                        Retry
                    </Button>
                }
            />
        );
    }

    if (!stats || stats.total === 0) {
        return (
            <Empty
                description="No annotations found for this task."
                image={Empty.PRESENTED_IMAGE_SIMPLE}
            />
        );
    }

    const maxCount = Math.max(...stats.classes.map((c) => c.count));

    return (
        <div className="cvat-task-annotation-stats">
            <Text strong>Annotation Statistics (Total: {stats.total})</Text>
            <div style={{ marginTop: '10px', maxHeight: '200px', overflowY: 'auto', paddingRight: '10px' }}>
                {stats.classes.map((cls) => {
                    const percent = maxCount > 0 ? Math.round((cls.count / maxCount) * 100) : 0;
                    return (
                        <Row key={cls.label_id} align="middle" style={{ marginBottom: '5px' }}>
                            <Col span={6}>
                                <Text ellipsis title={cls.name}>{cls.name}</Text>
                            </Col>
                            <Col span={14}>
                                <Progress
                                    percent={percent}
                                    showInfo={false}
                                    strokeColor={cls.color || '#1890ff'}
                                    strokeWidth={10}
                                />
                            </Col>
                            <Col span={4} style={{ textAlign: 'right' }}>
                                <Text type="secondary">{cls.count}</Text>
                            </Col>
                        </Row>
                    );
                })}
            </div>
        </div>
    );
}
