import React, { useEffect, useState } from "react";
import { csv } from "d3";
import CSVfile from "../data/Voltage.csv";
import SelectPlot from "./SelectPlot";
import Plot from "./PlotCompo";

const PlotComponent = () => {
  const [channel1, setChannel1] = useState([]);
  const [channel2, setChannel2] = useState([]);
  const [channel3, setChannel3] = useState([]);
  const [channel4, setChannel4] = useState([]);
  const [channel5, setChannel5] = useState([]);
  const [channel6, setChannel6] = useState([]);
  const [channel7, setChannel7] = useState([]);
  const [channel8, setChannel8] = useState([]);

  const [isOpen, setIsOpen] = useState(false);
  const [plotOptions, setPlotOptions] = useState({
    "Channel 1": true,
    "Channel 2": true,
    "Channel 3": true,
    "Channel 4": true,
    "Channel 5": true,
    "Channel 6": true,
    "Channel 7": true,
    "Channel 8": true,
  });

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    // temporary variables
    const CHANNEL1 = [];
    const CHANNEL2 = [];
    const CHANNEL3 = [];
    const CHANNEL4 = [];
    const CHANNEL5 = [];
    const CHANNEL6 = [];
    const CHANNEL7 = [];
    const CHANNEL8 = [];

    // load and set data
    csv(CSVfile).then(async (data) => {
      // Setting temporary variables
      let myData = limit(data);
      await myData.map(async (dat) => {
        if(dat["Channel1"]){
          CHANNEL1.push(dat["Channel1"]);
        }
        if(dat["Channel2"]){
          CHANNEL2.push(dat["Channel2"]);
        }
        if(dat["Channel3"]){
          CHANNEL3.push(dat["Channel3"]);
        }
        if(dat["Channel4"]){
          CHANNEL4.push(dat["Channel4"]);
        }
        if(dat["Channel5"]){
          CHANNEL5.push(dat["Channel5"]);
        }
        if(dat["Channel6"]){
          CHANNEL6.push(dat["Channel6"]);
        }
        if(dat["Channel7"]){
          CHANNEL7.push(dat["Channel7"]);
        }
        if(dat["Channel8"]){
          CHANNEL8.push(dat["Channel8"]);
        }
      });

      // Setting data to state variables
      setChannel1(CHANNEL1);
      setChannel2(CHANNEL2);
      setChannel3(CHANNEL3);
      setChannel4(CHANNEL4);
      setChannel5(CHANNEL5);
      setChannel6(CHANNEL6);
      setChannel7(CHANNEL7);
      setChannel8(CHANNEL8);
    });
  };

  // Limiting values
  const limit = (value) => {
    if (value?.length <= 6000) {
      return value;
    } else {
    
  return value?.slice(-6000);
    }
  };

  return (
    <div>
      <SelectPlot
        isOpen={isOpen}
        setIsOpen={setIsOpen}
        plotOptions={plotOptions}
        setPlotOptions={setPlotOptions}
      />

      <div className='row plots'>
        {plotOptions["Channel 1"] && (
          <Plot
            yData={channel1}
            color={"red"}
            title={"Voltage from channel 1"}
          />
        )}
        {plotOptions["Channel 2"] && (
          <Plot
            yData={channel2}
            color={"#01dbcd"}
            title={"Voltage from channel 2"}
          />
        )}
        {plotOptions["Channel 3"] && (
          <Plot
            yData={channel3}
            color={"violet"}
            title={"Voltage from channel 3"}
          />
        )}
        {plotOptions["Channel 4"] && (
          <Plot
            yData={channel4}
            color={"red"}
            title={"Voltage from channel 4"}
          />
        )}
        {plotOptions["Channel 5"] && (
          <Plot
            yData={channel5}
            color={"green"}
            title={"Voltage from channel 5"}
          />
        )}
        {plotOptions["Channel 6"] && (
          <Plot
            yData={channel6}
            color={"blue"}
            title={"Voltage from channel 6"}
          />
        )}
        {plotOptions["Channel 7"] && (
          <Plot
            yData={channel7}
            color={"pink"}
            title={"Voltage from channel 7"}
          />
        )}
        {plotOptions["Channel 8"] && (
          <Plot
            yData={channel8}
            color={"#aa1100"}
            title={"Voltage from channel 8"}
          />
        )}
      </div>
    </div>
  );
};

export default PlotComponent;
