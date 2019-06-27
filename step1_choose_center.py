#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
from plot import *
from cluster import *


def plot(data, auto_select_dc=False):
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # DPC物件 = 密度 + 高峰 + 叢集
    dpcluster = DensityPeakCluster()

    # 呼叫 DPC 的 local_density (局部密度)方法
    distances, max_dis, min_dis, max_id, rho = dpcluster.local_density(
        load_paperdata, data, auto_select_dc=auto_select_dc)
    # 返回 (1)距離dict (2)最大距離 (3)最小距離 (4)最大指數 (5)局部密度向量rho

    # 呼叫 DPC 的 min_distance (最小距離)方法
    delta, nneigh = min_distance(max_id, max_dis, distances, rho)
    # 返回 (1)最小距離向量delta (2)最近鄰居向量

    plot_rho_delta(rho, delta)  # plot to choose the threshold
    # rho = ρ = 局部密度 = X軸
    # delta = δ = 一個點和任何其他點之間的最小距離 = Y軸
    # 找出 高rho 和 高delta，它們是叢集中心。

if __name__ == '__main__':
    # plot('./data/data_in_paper/example_distances.dat')
    plot('./data/data_iris_flower/iris.forcluster', auto_select_dc=True)
