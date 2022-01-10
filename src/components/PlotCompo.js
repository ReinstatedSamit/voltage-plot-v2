import React, { useEffect } from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";


export default function PlotCompo({ yData, color, title, together }) {

  const data =[]

    yData.map(val=>{
      data.push({
        name:"voltage",
        value: val,
        n: 4000,
      })
    })
  
  return (
    <div className="col-md-4" >
      <div className='plot'>
     
        <LineChart
        width={500} height={300}
          data={data}
        >
          <CartesianGrid strokeDasharray="1 1" />
          <XAxis />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
                dataKey='value'
                stroke={color} />
           <Line
                dataKey='n'
                stroke='#000'/>
        </LineChart>
        
      </div>
    </div>
  );
}
