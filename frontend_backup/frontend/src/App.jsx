import PlanPanel from './components/PlanPanel'
import AgentCanvas from './components/AgentCanvas'
import ControlPanel from './components/ControlPanel'

function App() {
  return (
    <div className="h-screen w-full flex bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
      <div className="w-80 flex-shrink-0 border-r border-slate-800/50">
        <PlanPanel />
      </div>
      <div className="flex-1">
        <AgentCanvas />
      </div>
      <ControlPanel />
    </div>
  )
}

export default App
