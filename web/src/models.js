export const nor=(a,b)=>Number(!(a||b));
export const gates=(a,b)=>({NOR:nor(a,b),OR:Number(!!(a||b)),AND:a*b,NAND:1-a*b,XOR:a^b,XNOR:1-(a^b),NOT:1-a});
export function cavity(qi,qe,I,beta=.05,gamma=.01){const alpha=beta*I+gamma*I*I,qa=alpha?2*Math.PI*3.6/(.000155*alpha):Infinity,q=1/(1/qi+1/qe+1/qa);return {q,tau:q*1.55e-6/(2*Math.PI*299792458)*1e12,qa,eta:q/qe};}
export const overlap=(shift,angle)=>Math.exp(-4*(shift/1000)**2)*Math.cos(angle*Math.PI/180)**2;
export const coupler=(L,Lc)=>Math.sin(Math.PI*L/(2*Lc))**2;
export const mzi=phi=>Math.sin(phi/2)**2;
export const fanout=(f,loss,overlap)=>f*10**(loss/10)/overlap;
