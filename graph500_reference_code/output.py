def output(SCALE, NBFS, NSSSP, kernel_1_time, kernel_2_time, kernel_2_nedge):
    import numpy as np

    print("SCALE: %d" % SCALE)
    print("NBFS: %d" % NBFS)
    print("construction_time: %20.17e\n" % kernel_1_time)
    
    print("bfs_min_time: %20.17e" % np.percentile(kernel_2_time, 0))
    print("bfs_firstquartile_time: %20.17e" % np.percentile(kernel_2_time, 25))
    print("bfs_median_time: %20.17e" % np.percentile(kernel_2_time, 50))
    print("bfs_thirdquartile_time: %20.17e" % np.percentile(kernel_2_time, 75))
    print("bfs_max_time: %20.17e" % np.percentile(kernel_2_time, 100))
    print("bfs_mean_time: %20.17e" % np.mean(kernel_2_time))
    print("bfs_stddev_time: %20.17e\n" % np.std(kernel_2_time))
    
    #print("bfs_min_nedge: %20.17e" % np.percentile(kernel_2_nedge, 0))
    #print("bfs_firstquartile_nedge: %20.17e" % np.percentile(kernel_2_nedge, 25))
    #print("bfs_median_nedge: %20.17e" % np.percentile(kernel_2_nedge, 50))
    #print("bfs_thirdquartile_nedge: %20.17e" % np.percentile(kernel_2_nedge, 75))
    #print("bfs_max_nedge: %20.17e" % np.percentile(kernel_2_nedge, 100))
    #print("bfs_mean_nedge: %20.17e" % np.mean(kernel_2_nedge))
    #print("bfs_stddev_nedge: %20.17e\n" % np.std(kernel_2_nedge))
    
    #K2TEPS = kernel_2_nedge / kernel_2_time
    #print("bfs_min_TEPS: %20.17e" % np.percentile(K2TEPS, 0))
    #print("bfs_firstquartile_TEPS: %20.17e" % np.percentile(K2TEPS, 25))
    #print("bfs_median_TEPS: %20.17e" % np.percentile(K2TEPS, 50))
    #print("bfs_thirdquartile_TEPS: %20.17e" % np.percentile(K2TEPS, 75))
    #print("bfs_max_TEPS: %20.17e" % np.percentile(K2TEPS, 100))
    #print("bfs_mean_TEPS: %20.17e" % np.mean(K2TEPS))
    #print("bfs_stddev_TEPS: %20.17e\n" % np.std(K2TEPS))