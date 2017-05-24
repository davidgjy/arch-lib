/*
 * Copyright 1999-2015 dangdang.com.
 * <p>
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * </p>
 */

package com.dangdang.ddframe.job.lite.internal.listener;

import com.dangdang.ddframe.job.lite.api.listener.ElasticJobListener;
import com.dangdang.ddframe.job.lite.internal.config.RescheduleListenerManager;
import com.dangdang.ddframe.job.lite.internal.election.ElectionListenerManager;
import com.dangdang.ddframe.job.lite.internal.failover.FailoverListenerManager;
import com.dangdang.ddframe.job.lite.internal.guarantee.GuaranteeListenerManager;
import com.dangdang.ddframe.job.lite.internal.instance.ShutdownListenerManager;
import com.dangdang.ddframe.job.lite.internal.instance.TriggerListenerManager;
import com.dangdang.ddframe.job.lite.internal.sharding.ShardingListenerManager;
import com.dangdang.ddframe.job.lite.internal.storage.JobNodeStorage;
import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.unitils.util.ReflectionUtils;

import java.util.Collections;

import static org.mockito.Mockito.verify;

public class ListenerManagerTest {
    
    @Mock
    private JobNodeStorage jobNodeStorage;
    
    @Mock
    private ElectionListenerManager electionListenerManager;
    
    @Mock
    private ShardingListenerManager shardingListenerManager;
    
    @Mock
    private FailoverListenerManager failoverListenerManager;
    
    @Mock
    private ShutdownListenerManager shutdownListenerManager;
    
    @Mock
    private TriggerListenerManager triggerListenerManager;
    
    @Mock
    private RescheduleListenerManager rescheduleListenerManager;
    
    @Mock
    private GuaranteeListenerManager guaranteeListenerManager;
    
    @Mock
    private RegistryCenterConnectionStateListener regCenterConnectionStateListener;
    
    private final ListenerManager listenerManager = new ListenerManager(null, "test_job", Collections.<ElasticJobListener>emptyList());
    
    @Before
    public void setUp() throws NoSuchFieldException {
        MockitoAnnotations.initMocks(this);
        ReflectionUtils.setFieldValue(listenerManager, "jobNodeStorage", jobNodeStorage);
        ReflectionUtils.setFieldValue(listenerManager, "electionListenerManager", electionListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "shardingListenerManager", shardingListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "failoverListenerManager", failoverListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "shutdownListenerManager", shutdownListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "triggerListenerManager", triggerListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "rescheduleListenerManager", rescheduleListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "guaranteeListenerManager", guaranteeListenerManager);
        ReflectionUtils.setFieldValue(listenerManager, "regCenterConnectionStateListener", regCenterConnectionStateListener);
    }
    
    @Test
    public void assertStartAllListeners() {
        listenerManager.startAllListeners();
        verify(electionListenerManager).start();
        verify(shardingListenerManager).start();
        verify(failoverListenerManager).start();
        verify(shutdownListenerManager).start();
        verify(rescheduleListenerManager).start();
        verify(guaranteeListenerManager).start();
        verify(jobNodeStorage).addConnectionStateListener(regCenterConnectionStateListener);
    }
}
