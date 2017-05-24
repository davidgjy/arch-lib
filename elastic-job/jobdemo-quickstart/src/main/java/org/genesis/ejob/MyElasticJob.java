package org.genesis.ejob;

import com.dangdang.ddframe.job.api.ShardingContext;
import com.dangdang.ddframe.job.api.simple.SimpleJob;

/**
 * Created by KG on 2017/5/4.
 */
public class MyElasticJob implements SimpleJob {
    public void execute(ShardingContext context) {
        switch (context.getShardingItem()) {
            case 0:
                // do something by sharding item 0
                System.out.println("shard 0");
                break;
            case 1:
                // do something by sharding item 1
                System.out.println("shard 1");
                break;
            case 2:
                // do something by sharding item 2
                System.out.println("shard 2");
                break;
            // case n: ...
        }
    }
}
