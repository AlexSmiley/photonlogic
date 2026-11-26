import test from 'node:test';import assert from 'node:assert/strict';import {gates,cavity,overlap,coupler,mzi,fanout} from './models.js';
test('NOR truth table',()=>{for(let a of [0,1])for(let b of [0,1])assert.equal(gates(a,b).NOR,1-Number(!!(a||b)))});
test('cavity',()=>assert.ok(cavity(8000,889,10).q<800));
test('overlap',()=>assert.equal(overlap(0,0),1));
test('coupler',()=>assert.equal(coupler(10,10),1));
test('MZI',()=>assert.equal(mzi(Math.PI),1));
test('fanout',()=>assert.equal(fanout(4,0,.5),8));
