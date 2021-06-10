package com.zjhw.hbase.homework;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.util.Bytes;

import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Dryhten {
    public static void main(String[] args) throws IOException {
        Configuration conf = new HBaseConfiguration();
        //链接hbase
        conf.set("hbase.zookeeper.quorum","ddcva,dddva,ddeva");
        FileSystem fs = FileSystem.get(conf);
        HBaseAdmin hBaseAdmin = new HBaseAdmin(conf);
        TableName tableName = TableName.valueOf("rg2020650117_stu");
        if(hBaseAdmin.tableExists(tableName)) {
            if (hBaseAdmin.isTableAvailable(tableName)) {
                hBaseAdmin.disableTable(tableName);
            }
            hBaseAdmin.deleteTable(tableName);
        }
        HTableDescriptor htd = new HTableDescriptor(tableName);
        htd.addFamily(new HColumnDescriptor("info"));
        htd.addFamily(new HColumnDescriptor("score"));
        hBaseAdmin.createTable(htd);
        System.out.println(tableName+"表创建成功");
        Path path1 = new Path("/home/student");
        FSDataInputStream dos1 = fs.open(path1);
        BufferedReader bw = new BufferedReader(new InputStreamReader(dos1));
        System.out.println("获取/home/student文件成功");
        String title = bw.readLine();
        String line1 = bw.readLine();
        String line2 = bw.readLine();
        String line3 = bw.readLine();
        String line4 = bw.readLine();
        System.out.println("按行读取文件信息成功");
        List<String> Title = Arrays.asList(title.split(","));
        List<String> result1 = Arrays.asList(line1.split(","));
        List<String> result2 = Arrays.asList(line2.split(","));
        List<String> result3 = Arrays.asList(line3.split(","));
        List<String> result4 = Arrays.asList(line4.split(","));
        System.out.println("分离元素值成功成功");
        HTable hTable = new HTable(conf, tableName);
        Put put1= new Put(Bytes.toBytes("row1"));
        put1.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(1)),Bytes.toBytes(result1.get(1)));
        put1.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(2)),Bytes.toBytes(result1.get(2)));
        put1.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(3)),Bytes.toBytes(result1.get(3)));
        put1.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(4)),Bytes.toBytes(result1.get(4)));
        put1.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(5)),Bytes.toBytes(result1.get(5)));
        put1.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(6)),Bytes.toBytes(result1.get(6)));

        Put put2= new Put(Bytes.toBytes("row2"));
        put2.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(1)),Bytes.toBytes(result2.get(1)));
        put2.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(2)),Bytes.toBytes(result2.get(2)));
        put2.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(3)),Bytes.toBytes(result2.get(3)));
        put2.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(4)),Bytes.toBytes(result2.get(4)));
        put2.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(5)),Bytes.toBytes(result2.get(5)));
        put2.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(6)),Bytes.toBytes(result2.get(6)));

        Put put3= new Put(Bytes.toBytes("row3"));
        put3.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(1)),Bytes.toBytes(result3.get(1)));
        put3.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(2)),Bytes.toBytes(result3.get(2)));
        put3.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(3)),Bytes.toBytes(result3.get(3)));
        put3.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(4)),Bytes.toBytes(result3.get(4)));
        put3.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(5)),Bytes.toBytes(result3.get(5)));
        put3.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(6)),Bytes.toBytes(result3.get(6)));

        Put put4= new Put(Bytes.toBytes("row4"));
        put4.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(1)),Bytes.toBytes(result4.get(1)));
        put4.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(2)),Bytes.toBytes(result4.get(2)));
        put4.add(Bytes.toBytes("info"),Bytes.toBytes(Title.get(3)),Bytes.toBytes(result4.get(3)));
        put4.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(4)),Bytes.toBytes(result4.get(4)));
        put4.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(5)),Bytes.toBytes(result4.get(5)));
        put4.add(Bytes.toBytes("score"),Bytes.toBytes(Title.get(6)),Bytes.toBytes(result4.get(6)));

        List<Put> list = new ArrayList<Put>();
        list.add(put1);
        list.add(put2);
        list.add(put3);
        list.add(put4);
        hTable.put(list);
        System.out.println("插入成功");
    }
}
