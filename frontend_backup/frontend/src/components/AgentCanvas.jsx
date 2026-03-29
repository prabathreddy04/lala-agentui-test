export default function AgentCanvas() {
  return (
    <div className="h-full flex flex-col">
      <div className="px-5 py-4 border-b border-slate-800/50 bg-slate-900/30 backdrop-blur-sm">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
          <h2 className="text-base font-semibold text-slate-100 tracking-wide">Agent Canvas</h2>
        </div>
      </div>
      <div className="flex-1 flex items-center justify-center relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-slate-800/10 to-transparent" />
        <div className="relative">
          <div className="w-20 h-20 rounded-2xl bg-slate-800/30 border border-slate-700/50 flex items-center justify-center mb-4">
            <svg className="w-8 h-8 text-slate-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
          </div>
          <p className="text-slate-500 text-sm font-medium tracking-wide">Canvas Area</p>
        </div>
      </div>
    </div>
  )
}
