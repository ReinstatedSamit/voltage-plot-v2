import React, { useState } from "react";
import Switch from "@mui/material/Switch";

const EnableOption = ({ op, plotOptions, setPlotOptions }) => {
  let obj = plotOptions;

  const [option, setOption] = useState(plotOptions[op]);

  const handleChange = () => {
    setOption(!option);
    obj[op] = !obj[op];
    setPlotOptions(obj);
  };

  return (
    <li className='option'>
      <p>{op} </p>
      <div type='reset'>
        <Switch
          checked={option}
          onChange={() => handleChange()}
          inputProps={{ "aria-label": "controlled" }}
          color='warning'
        />
      </div>
    </li>
  );
};

export default EnableOption;
