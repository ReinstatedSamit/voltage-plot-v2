import React from "react";
import EnableOption from "./EnableOption";

const SelectPlot = ({ isOpen, setIsOpen, plotOptions, setPlotOptions }) => {
  return (
    <div>
      <div className='select__plots'>
        <button
          className='btn-lg btn-info my-3'
          onClick={() => setIsOpen(true)}>
          SELECT VISIBLE PLOTS
        </button>
        {isOpen && (
          <div className='optionsWindow'>
            <div className='options__card'>
              <div className=''>
                <button
                  onClick={() => setIsOpen(false)}
                  className='btn btn-danger m-auto cross_button'>
                  Close
                </button>
              </div>

              {/*Toggle Buttons*/}

              <ul className='options'>
                {Object.keys(plotOptions)?.map((op, key) => (
                  <EnableOption
                    key={key}
                    op={op}
                    plotOptions={plotOptions}
                    setPlotOptions={setPlotOptions}
                  />
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SelectPlot;
