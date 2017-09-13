# JavaScript Research Project Calculator

This file is part of The JavaScript Research Project Calculator (JRPC).

JRPC is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

JRPC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with The RPC.  If not, see <http://www.gnu.org/licenses/>.

## Installation Instructions

Download the jrpc.js, jrpc.html, and jrpc.css files. Rename the html file as appropriate. Modify the RPC steps, and correlating text in the jrpc.js file as wanted. 

The HTML file is a basic template that can be changed as appropriate. Currently it is setup for 8 steps.

To add a step, copy the step8Panel and rename any instances of '8' to '9'. You can also remove steps. 
Remember, the number of steps in the jrpc.html file needs to correlate to the number of steps in the jrpc.js file. So, StepTimes, StepBody, StepTitles all need to have the same number of steps.
Remember, concerning StepTimes - The decimal point describes the amount of time each step should take. Make sure that the total of your numbers equal 1 (one), or in other words make sure it equals 100% of the time.

## Requirements

<a href="https://jquery.com/">jQuery</a>, <a href="http://jqueryui.com/">jQuery-ui</a>, <a href="http://getbootstrap.com/">Bootstrap</a>, <a href="http://momentjs.com/">Moment.js</a>

## Acknowledgements

Based on the <a target="_blank" href="http://www.lib.umn.edu">University of Minnesota Libraries</a>' <a target="_blank" href="https://github.com/ac-rpc/ac-rpc-core">Assignment Calculator</a>.
  
## TODO:

Add google cal functionality? Print friendly version? Add txt or email? Download to pdf? iframe into LibGuides?

Easier to add to webpage? <script jrpc.js></script><div id="jrpc"></div>
Model after: https://doaj.org/widgets
