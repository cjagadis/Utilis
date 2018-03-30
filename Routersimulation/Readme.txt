Simulation of a Routing
1. Loadbalancer forwards request from Application Server to RouterAgent
2. RouterAgents parses the requests and calls any of the switcher servers to allocate resources
3. RourterAgents sends the request for allocation to RouterSwitchAgents which are on all
switchers
4. RouterSwitchAgents parse the request for RouterAgents and allocate resources after updating
global and internal data structurs about the allocation. And return the status of allocated
request to RouterAgent
