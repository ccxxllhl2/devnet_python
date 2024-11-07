use std::collections::HashMap;

fn main() {
    // 定义接口数据
    let interfaces_msg = vec![
        [("name", "ge0/0"), ("description", "manager"), ("status", "up")],
        [("name", "ge0/1"), ("description", "core01"), ("status", "up")],
        [("name", "ge0/2"), ("description", "core02"), ("status", "up")],
        [("name", "ge0/3"), ("description", "branch01"), ("status", "up")],
        [("name", "ge0/4"), ("description", "branch02"), ("status", "up")],
    ];

    // 定义IP数据
    let mut ip_datas = HashMap::new();
    ip_datas.insert("interface0", "10.10.10.1");
    ip_datas.insert("interface1", "172.16.1.1");
    ip_datas.insert("interface2", "172.17.1.1");
    ip_datas.insert("interface3", "172.18.1.1");
    ip_datas.insert("interface4", "192.168.25.1");

    // 遍历接口信息
    for (int_index, interface) in interfaces_msg.iter().enumerate() {
        let int_name = interface[0].1;
        let int_des = interface[1].1;
        let int_status = interface[2].1;

        // 使用临时变量来存储格式化的字符串，确保其生命周期足够长
        let key = format!("interface{}", int_index);
        let int_ip = ip_datas.get(key.as_str()).unwrap_or(&"未知IP");

        // 打印信息
        println!("{} 接口 {} 目前的状态是 {}，其IP地址为：{}", int_des, int_name, int_status, int_ip);
    }
}
