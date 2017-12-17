__all__ = ['calculo']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['D50', 'H50', 'F55LV', 'F51U', 'tvfmfs_comment', 'ZGRI', 'round_power', 'VGRID', 'F55HV', 'H10', 'F51HV', 'F51LV', 'tvfmfs_metric', 'fzq', 'F55U', 'D10', 'itplbv'])
@Js
def PyJsHoisted_itplbv_(lx, ly, x, y, z, n, u, v, w, this, arguments, var=var):
    var = Scope({'lx':lx, 'ly':ly, 'x':x, 'y':y, 'z':z, 'n':n, 'u':u, 'v':v, 'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['z32', 'z34', 'wy3', 'a3sq', 'za_row1', 'v', 'w3', 'y2', 'y5', 'za_row2', 'zxy', 'zb_row1', 'zxy_row1', 'p30', 'lyp1', 'n', 'lxm1', 'zab_row0', 'b3sq', 'lx', 'b', 'za_row4', 'zxy_row3', 'p21', 'iy', 'imx', 'jx1', 'zb_row0', 'z33', 'ixpv', 'w', 'zab_row2', 'y3', 'zb', 'w4', 'x3', 'zx3b3', 'b2', 'wy2', 'zx_row3', 'z44', 'k', 'a', 'p02', 'iypv', 'c', 'y', 'zy_row3', 'z24', 'jy1', 'p33', 'zx', 'z43', 'imn', 'p12', 'd', 'ly', 'zx_row0', 'a1', 'b1', 'z42', 'sw', 'zy_row1', 'w5', 'p22', 'z54', 'q2', 'x2', 'p03', 'x', 'z23', 'a3', 'w1', 'zy', 'zy_row2', 'a5', 'x5', 'ix', 'w2', 'zab', 'zy_row0', 'za_row0', 'dy', 'b5', 'z45', 'wx3', 'p31', 'wx2', 'p13', 'jx', 'q0', 'a4', 'x4', 'zab_row1', 'zx_row2', 'zxy_row0', 'zxy_row2', 'zx_row1', 'y4', 'jy', 'zy3a3', 'dx', 'p32', 'zx4b3', 'za', 'lxp1', 'z', 'zy4a3', 'q3', 'u', 'z53', 'b3', 'za_row3', 'b4', 'lym1', 'q1', 'e', 'a2', 'p23', 'z35', 'p20'])
    pass
    var.put('lxm1', var.put('lxp1', var.put('lym1', var.put('lyp1', var.put('ixpv', var.put('iypv', var.put('k', var.put('ix', var.put('iy', var.put('imn', var.put('imx', var.put('jx', var.put('jy', var.put('jx1', var.put('jy1', Js(0.0))))))))))))))))
    var.put('za_row0', Js([Js(0.0), Js(0.0)]))
    var.put('za_row1', Js([Js(0.0), Js(0.0)]))
    var.put('za_row2', Js([Js(0.0), Js(0.0)]))
    var.put('za_row3', Js([Js(0.0), Js(0.0)]))
    var.put('za_row4', Js([Js(0.0), Js(0.0)]))
    var.put('za', Js([var.get('za_row0'), var.get('za_row1'), var.get('za_row2'), var.get('za_row3'), var.get('za_row4')]))
    var.put('zb_row0', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zb_row1', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zb', Js([var.get('zb_row0'), var.get('zb_row1')]))
    var.put('zab_row0', Js([Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zab_row1', Js([Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zab_row2', Js([Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zab', Js([var.get('zab_row0'), var.get('zab_row1'), var.get('zab_row2')]))
    var.put('zx_row0', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zx_row1', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zx_row2', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zx_row3', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zx', Js([var.get('zx_row0'), var.get('zx_row1'), var.get('zx_row2'), var.get('zx_row3')]))
    var.put('zy_row0', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zy_row1', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zy_row2', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zy_row3', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zy', Js([var.get('zy_row0'), var.get('zy_row1'), var.get('zy_row2'), var.get('zy_row3')]))
    var.put('zxy_row0', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zxy_row1', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zxy_row2', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zxy_row3', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('zxy', Js([var.get('zxy_row0'), var.get('zxy_row1'), var.get('zxy_row2'), var.get('zxy_row3')]))
    pass
    var.put('x3', var.put('x4', var.put('a3', var.put('y3', var.put('y4', var.put('b3', var.put('z33', var.put('z43', var.put('z34', var.put('z44', var.put('x2', var.put('a2', var.put('z23', var.put('z24', var.put('x5', var.put('a4', var.put('z53', var.put('z54', Js(0.0)))))))))))))))))))
    pass
    var.put('a1', var.put('a5', var.put('y2', var.put('b2', var.put('z32', var.put('z42', var.put('y5', var.put('b4', var.put('z35', var.put('z45', var.put('b1', var.put('b5', var.put('w2', var.put('w3', var.put('sw', var.put('wx2', var.put('wx3', var.put('wy2', var.put('wy3', var.put('w1', var.put('w4', var.put('w5', Js(0.0)))))))))))))))))))))))
    pass
    var.put('zx3b3', var.put('zx4b3', var.put('zy3a3', var.put('zy4a3', var.put('a', var.put('b', var.put('c', var.put('d', var.put('e', var.put('a3sq', var.put('b3sq', var.put('p02', var.put('p03', var.put('p12', var.put('p13', var.put('p20', var.put('p21', var.put('p22', Js(0.0)))))))))))))))))))
    pass
    var.put('p23', var.put('p30', var.put('p31', var.put('p32', var.put('p33', var.put('dy', var.put('q0', var.put('q1', var.put('q2', var.put('q3', var.put('dx', Js(0.0))))))))))))
    var.put('lx', var.get('Math').callprop('floor', var.get('lx')))
    var.put('ly', var.get('Math').callprop('floor', var.get('ly')))
    var.put('lxm1', var.get('Math').callprop('floor', (var.get('lx')-Js(1.0))))
    var.put('lxp1', var.get('Math').callprop('floor', (var.get('lx')+Js(1.0))))
    var.put('lym1', var.get('Math').callprop('floor', (var.get('ly')-Js(1.0))))
    var.put('lyp1', var.get('Math').callprop('floor', (var.get('ly')+Js(1.0))))
    var.put('ixpv', (-Js(1.0)))
    var.put('iypv', (-Js(1.0)))
    #for JS loop
    var.put('k', Js(0.0))
    while (var.get('k')<var.get('n')):
        try:
            if (var.get('u').get(var.get('k'))>=var.get('x').get(var.get('lxm1'))):
                var.put('ix', var.get('lx'))
            else:
                if (var.get('u').get(var.get('k'))<var.get('x').get('0')):
                    var.put('ix', Js(0.0))
                else:
                    var.put('imn', Js(1.0))
                    var.put('imx', var.get('lxm1'))
                    while 1:
                        var.put('ix', var.get('Math').callprop('floor', ((var.get('imn')+var.get('imx'))/Js(2.0))))
                        if (var.get('u').get(var.get('k'))>=var.get('x').get(var.get('ix'))):
                            var.put('imn', (var.get('ix')+Js(1.0)))
                        else:
                            var.put('imx', var.get('ix'))
                        if not (var.get('imx')>var.get('imn')):
                            break
                    var.put('ix', var.get('imx'))
            var.put('ix', var.get('Math').callprop('floor', var.get('ix')))
            if (var.get('v').get(var.get('k'))>=var.get('y').get(var.get('lym1'))):
                var.put('iy', var.get('ly'))
            else:
                if (var.get('v').get(var.get('k'))<var.get('y').get('0')):
                    var.put('iy', Js(0.0))
                else:
                    var.put('imn', Js(1.0))
                    var.put('imx', var.get('lym1'))
                    while 1:
                        var.put('iy', var.get('Math').callprop('floor', ((var.get('imn')+var.get('imx'))/Js(2.0))))
                        if (var.get('v').get(var.get('k'))>=var.get('y').get(var.get('iy'))):
                            var.put('imn', (var.get('iy')+Js(1.0)))
                        else:
                            var.put('imx', var.get('iy'))
                        if not (var.get('imx')>var.get('imn')):
                            break
                    var.put('iy', var.get('imx'))
            var.put('iy', var.get('Math').callprop('floor', var.get('iy')))
            if ((var.get('ix')!=var.get('ixpv')) or (var.get('iy')!=var.get('iypv'))):
                var.put('ixpv', var.get('ix'))
                var.put('iypv', var.get('iy'))
                if (var.get('ix')==Js(0.0)):
                    var.put('jx', Js(1.0))
                else:
                    if (var.get('ix')==var.get('lx')):
                        var.put('jx', var.get('lxm1'))
                    else:
                        var.put('jx', var.get('ix'))
                if (var.get('iy')==Js(0.0)):
                    var.put('jy', Js(1.0))
                else:
                    if (var.get('iy')==var.get('ly')):
                        var.put('jy', var.get('lym1'))
                    else:
                        var.put('jy', var.get('iy'))
                var.put('jx', var.get('Math').callprop('floor', var.get('jx')))
                var.put('jy', var.get('Math').callprop('floor', var.get('jy')))
                var.put('x3', var.get('x').get((var.get('jx')-Js(1.0))))
                var.put('x4', var.get('x').get(var.get('jx')))
                var.put('a3', (Js(1.0)/(var.get('x4')-var.get('x3'))))
                var.put('y3', var.get('y').get((var.get('jy')-Js(1.0))))
                var.put('y4', var.get('y').get(var.get('jy')))
                var.put('b3', (Js(1.0)/(var.get('y4')-var.get('y3'))))
                var.put('z33', var.get('z').get(((var.get('jx')-Js(1.0))+((var.get('jy')-Js(1.0))*var.get('lx')))))
                var.put('z43', var.get('z').get((var.get('jx')+((var.get('jy')-Js(1.0))*var.get('lx')))))
                var.put('z34', var.get('z').get(((var.get('jx')-Js(1.0))+(var.get('jy')*var.get('lx')))))
                var.put('z44', var.get('z').get((var.get('jx')+(var.get('jy')*var.get('lx')))))
                var.get('za').get('2').put('0', ((var.get('z43')-var.get('z33'))*var.get('a3')))
                var.get('za').get('2').put('1', ((var.get('z44')-var.get('z34'))*var.get('a3')))
                var.get('zb').get('0').put('2', ((var.get('z34')-var.get('z33'))*var.get('b3')))
                var.get('zb').get('1').put('2', ((var.get('z44')-var.get('z43'))*var.get('b3')))
                var.get('zab').get('1').put('1', ((var.get('zb').get('1').get('2')-var.get('zb').get('0').get('2'))*var.get('a3')))
                if (var.get('jx')>Js(1.0)):
                    var.put('x2', var.get('x').get((var.get('jx')-Js(2.0))))
                    var.put('a2', (Js(1.0)/(var.get('x3')-var.get('x2'))))
                    var.put('z23', var.get('z').get(((var.get('jx')-Js(2.0))+((var.get('jy')-Js(1.0))*var.get('lx')))))
                    var.put('z24', var.get('z').get(((var.get('jx')-Js(2.0))+(var.get('jy')*var.get('lx')))))
                    var.get('za').get('1').put('0', ((var.get('z33')-var.get('z23'))*var.get('a2')))
                    var.get('za').get('1').put('1', ((var.get('z34')-var.get('z24'))*var.get('a2')))
                    if (var.get('jx')==var.get('lxm1')):
                        var.get('za').get('3').put('0', ((Js(2.0)*var.get('za').get('2').get('0'))-var.get('za').get('1').get('0')))
                        var.get('za').get('3').put('1', ((Js(2.0)*var.get('za').get('2').get('1'))-var.get('za').get('1').get('1')))
                if (var.get('jx')<var.get('lxm1')):
                    var.put('x5', var.get('x').get((var.get('jx')+Js(1.0))))
                    var.put('a4', (Js(1.0)/(var.get('x5')-var.get('x4'))))
                    var.put('z53', var.get('z').get(((var.get('jx')+Js(1.0))+((var.get('jy')-Js(1.0))*var.get('lx')))))
                    var.put('z54', var.get('z').get(((var.get('jx')+Js(1.0))+(var.get('jy')*var.get('lx')))))
                    var.get('za').get('3').put('0', ((var.get('z53')-var.get('z43'))*var.get('a4')))
                    var.get('za').get('3').put('1', ((var.get('z54')-var.get('z44'))*var.get('a4')))
                    if (var.get('jx')==Js(1.0)):
                        var.get('za').get('1').put('0', ((Js(2.0)*var.get('za').get('2').get('0'))-var.get('za').get('3').get('0')))
                        var.get('za').get('1').put('1', ((Js(2.0)*var.get('za').get('2').get('1'))-var.get('za').get('3').get('1')))
                var.get('zab').get('0').put('1', ((var.get('za').get('1').get('1')-var.get('za').get('1').get('0'))*var.get('b3')))
                var.get('zab').get('2').put('1', ((var.get('za').get('3').get('1')-var.get('za').get('3').get('0'))*var.get('b3')))
                if (var.get('jx')>Js(2.0)):
                    var.put('a1', (Js(1.0)/(var.get('x2')-var.get('x').get((var.get('jx')-Js(3.0))))))
                    var.get('za').get('0').put('0', ((var.get('z23')-var.get('z').get(((var.get('jx')-Js(3.0))+((var.get('jy')-Js(1.0))*var.get('lx')))))*var.get('a1')))
                    var.get('za').get('0').put('1', ((var.get('z24')-var.get('z').get(((var.get('jx')-Js(3.0))+(var.get('jy')*var.get('lx')))))*var.get('a1')))
                else:
                    var.get('za').get('0').put('0', ((Js(2.0)*var.get('za').get('1').get('0'))-var.get('za').get('2').get('0')))
                    var.get('za').get('0').put('1', ((Js(2.0)*var.get('za').get('1').get('1'))-var.get('za').get('2').get('1')))
                if (var.get('jx')<(var.get('lx')-Js(2.0))):
                    var.put('a5', (Js(1.0)/(var.get('x').get((var.get('jx')+Js(2.0)))-var.get('x5'))))
                    var.get('za').get('4').put('0', ((var.get('z').get(((var.get('jx')+Js(2.0))+((var.get('jy')-Js(1.0))*var.get('lx'))))-var.get('z53'))*var.get('a5')))
                    var.get('za').get('4').put('1', ((var.get('z').get(((var.get('jx')+Js(2.0))+(var.get('jy')*var.get('lx'))))-var.get('z54'))*var.get('a5')))
                else:
                    var.get('za').get('4').put('0', ((Js(2.0)*var.get('za').get('3').get('0'))-var.get('za').get('2').get('0')))
                    var.get('za').get('4').put('1', ((Js(2.0)*var.get('za').get('3').get('1'))-var.get('za').get('2').get('1')))
                if (var.get('jy')>Js(1.0)):
                    var.put('y2', var.get('y').get((var.get('jy')-Js(2.0))))
                    var.put('b2', (Js(1.0)/(var.get('y3')-var.get('y2'))))
                    var.put('z32', var.get('z').get(((var.get('jx')-Js(1.0))+((var.get('jy')-Js(2.0))*var.get('lx')))))
                    var.put('z42', var.get('z').get((var.get('jx')+((var.get('jy')-Js(2.0))*var.get('lx')))))
                    var.get('zb').get('0').put('1', ((var.get('z33')-var.get('z32'))*var.get('b2')))
                    var.get('zb').get('1').put('1', ((var.get('z43')-var.get('z42'))*var.get('b2')))
                    if (var.get('jy')==var.get('lym1')):
                        var.get('zb').get('0').put('3', ((Js(2.0)*var.get('zb').get('0').get('2'))-var.get('zb').get('0').get('1')))
                        var.get('zb').get('1').put('3', ((Js(2.0)*var.get('zb').get('1').get('2'))-var.get('zb').get('1').get('1')))
                if (var.get('jy')<var.get('lym1')):
                    var.put('y5', var.get('y').get((var.get('jy')+Js(1.0))))
                    var.put('b4', (Js(1.0)/(var.get('y5')-var.get('y4'))))
                    var.put('z35', var.get('z').get(((var.get('jx')-Js(1.0))+((var.get('jy')+Js(1.0))*var.get('lx')))))
                    var.put('z45', var.get('z').get((var.get('jx')+((var.get('jy')+Js(1.0))*var.get('lx')))))
                    var.get('zb').get('0').put('3', ((var.get('z35')-var.get('z34'))*var.get('b4')))
                    var.get('zb').get('1').put('3', ((var.get('z45')-var.get('z44'))*var.get('b4')))
                    if (var.get('jy')==Js(1.0)):
                        var.get('zb').get('0').put('1', ((Js(2.0)*var.get('zb').get('0').get('2'))-var.get('zb').get('0').get('3')))
                        var.get('zb').get('1').put('1', ((Js(2.0)*var.get('zb').get('1').get('2'))-var.get('zb').get('1').get('3')))
                var.get('zab').get('1').put('0', ((var.get('zb').get('1').get('1')-var.get('zb').get('0').get('1'))*var.get('a3')))
                var.get('zab').get('1').put('2', ((var.get('zb').get('1').get('3')-var.get('zb').get('0').get('3'))*var.get('a3')))
                if (var.get('jy')>Js(2.0)):
                    var.put('b1', (Js(1.0)/(var.get('y2')-var.get('y').get((var.get('jy')-Js(3.0))))))
                    var.get('zb').get('0').put('0', ((var.get('z32')-var.get('z').get(((var.get('jx')-Js(1.0))+((var.get('jy')-Js(3.0))*var.get('lx')))))*var.get('b1')))
                    var.get('zb').get('1').put('0', ((var.get('z42')-var.get('z').get((var.get('jx')+((var.get('jy')-Js(3.0))*var.get('lx')))))*var.get('b1')))
                else:
                    var.get('zb').get('0').put('0', ((Js(2.0)*var.get('zb').get('0').get('1'))-var.get('zb').get('0').get('2')))
                    var.get('zb').get('1').put('0', ((Js(2.0)*var.get('zb').get('1').get('1'))-var.get('zb').get('1').get('2')))
                if (var.get('jy')<(var.get('ly')-Js(2.0))):
                    var.put('b5', (Js(1.0)/(var.get('y').get((var.get('jy')+Js(2.0)))-var.get('y5'))))
                    var.get('zb').get('0').put('4', ((var.get('z').get(((var.get('jx')-Js(1.0))+((var.get('jy')+Js(2.0))*var.get('lx'))))-var.get('z35'))*var.get('b5')))
                    var.get('zb').get('1').put('4', ((var.get('z').get((var.get('jx')+((var.get('jy')+Js(2.0))*var.get('lx'))))-var.get('z45'))*var.get('b5')))
                else:
                    var.get('zb').get('0').put('4', ((Js(2.0)*var.get('zb').get('0').get('3'))-var.get('zb').get('0').get('2')))
                    var.get('zb').get('1').put('4', ((Js(2.0)*var.get('zb').get('1').get('3'))-var.get('zb').get('1').get('2')))
                if (var.get('jx')<var.get('lxm1')):
                    if (var.get('jy')>Js(1.0)):
                        var.get('zab').get('2').put('0', ((((var.get('z53')-var.get('z').get(((var.get('jx')+Js(1.0))+((var.get('jy')-Js(2.0))*var.get('lx')))))*var.get('b2'))-var.get('zb').get('1').get('1'))*var.get('a4')))
                        if (var.get('jy')<var.get('lym1')):
                            var.get('zab').get('2').put('2', ((((var.get('z').get(((var.get('jx')+Js(1.0))+((var.get('jy')+Js(1.0))*var.get('lx'))))-var.get('z54'))*var.get('b4'))-var.get('zb').get('1').get('3'))*var.get('a4')))
                        else:
                            var.get('zab').get('2').put('2', ((Js(2.0)*var.get('zab').get('2').get('1'))-var.get('zab').get('2').get('0')))
                    else:
                        var.get('zab').get('2').put('2', ((((var.get('z').get(((var.get('jx')+Js(1.0))+((var.get('jy')+Js(1.0))*var.get('lx'))))-var.get('z54'))*var.get('b4'))-var.get('zb').get('1').get('3'))*var.get('a4')))
                        var.get('zab').get('2').put('0', ((Js(2.0)*var.get('zab').get('2').get('1'))-var.get('zab').get('2').get('2')))
                    if (var.get('jx')==Js(1.0)):
                        var.get('zab').get('0').put('0', ((Js(2.0)*var.get('zab').get('1').get('0'))-var.get('zab').get('2').get('0')))
                        var.get('zab').get('0').put('2', ((Js(2.0)*var.get('zab').get('1').get('2'))-var.get('zab').get('2').get('2')))
                if (var.get('jx')>Js(1.0)):
                    if (var.get('jy')>Js(1.0)):
                        var.get('zab').get('0').put('0', ((var.get('zb').get('0').get('1')-((var.get('z23')-var.get('z').get(((var.get('jx')-Js(2.0))+((var.get('jy')-Js(2.0))*var.get('lx')))))*var.get('b2')))*var.get('a2')))
                        if (var.get('jy')<var.get('lym1')):
                            var.get('zab').get('0').put('2', ((var.get('zb').get('0').get('3')-((var.get('z').get(((var.get('jx')-Js(2.0))+((var.get('jy')+Js(1.0))*var.get('lx'))))-var.get('z24'))*var.get('b4')))*var.get('a2')))
                        else:
                            var.get('zab').get('0').put('2', ((Js(2.0)*var.get('zab').get('0').get('1'))-var.get('zab').get('0').get('0')))
                    else:
                        var.get('zab').get('0').put('2', ((var.get('zb').get('0').get('3')-((var.get('z').get(((var.get('jx')-Js(2.0))+((var.get('jy')+Js(1.0))*var.get('lx'))))-var.get('z24'))*var.get('b4')))*var.get('a2')))
                        var.get('zab').get('0').put('0', ((Js(2.0)*var.get('zab').get('0').get('1'))-var.get('zab').get('0').get('2')))
                    if (var.get('jx')==var.get('lxm1')):
                        var.get('zab').get('2').put('0', ((Js(2.0)*var.get('zab').get('1').get('0'))-var.get('zab').get('0').get('0')))
                        var.get('zab').get('2').put('2', ((Js(2.0)*var.get('zab').get('1').get('2'))-var.get('zab').get('0').get('2')))
                #for JS loop
                var.put('jy', Js(1.0))
                while (var.get('jy')<Js(3.0)):
                    try:
                        #for JS loop
                        var.put('jx', Js(1.0))
                        while (var.get('jx')<Js(3.0)):
                            try:
                                var.put('w2', var.get('Math').callprop('abs', (var.get('za').get((var.get('jx')+Js(2.0))).get((var.get('jy')-Js(1.0)))-var.get('za').get((var.get('jx')+Js(1.0))).get((var.get('jy')-Js(1.0))))))
                                var.put('w3', var.get('Math').callprop('abs', (var.get('za').get(var.get('jx')).get((var.get('jy')-Js(1.0)))-var.get('za').get((var.get('jx')-Js(1.0))).get((var.get('jy')-Js(1.0))))))
                                var.put('sw', (var.get('w2')+var.get('w3')))
                                if (var.get('sw')>=Js(1e-07)):
                                    var.put('wx2', (var.get('w2')/var.get('sw')))
                                    var.put('wx3', (var.get('w3')/var.get('sw')))
                                else:
                                    var.put('wx2', Js(0.5))
                                    var.put('wx3', Js(0.5))
                                var.get('zx').get(var.get('jx')).put(var.get('jy'), ((var.get('wx2')*var.get('za').get(var.get('jx')).get((var.get('jy')-Js(1.0))))+(var.get('wx3')*var.get('za').get((var.get('jx')+Js(1.0))).get((var.get('jy')-Js(1.0))))))
                                var.put('w2', var.get('Math').callprop('abs', (var.get('zb').get((var.get('jx')-Js(1.0))).get((var.get('jy')+Js(2.0)))-var.get('zb').get((var.get('jx')-Js(1.0))).get((var.get('jy')+Js(1.0))))))
                                var.put('w3', var.get('Math').callprop('abs', (var.get('zb').get((var.get('jx')-Js(1.0))).get(var.get('jy'))-var.get('zb').get((var.get('jx')-Js(1.0))).get((var.get('jy')-Js(1.0))))))
                                var.put('sw', (var.get('w2')+var.get('w3')))
                                if (var.get('sw')>=Js(1e-07)):
                                    var.put('wy2', (var.get('w2')/var.get('sw')))
                                    var.put('wy3', (var.get('w3')/var.get('sw')))
                                else:
                                    var.put('wy2', Js(0.5))
                                    var.put('wy3', Js(0.5))
                                var.get('zy').get(var.get('jx')).put(var.get('jy'), ((var.get('wy2')*var.get('zb').get((var.get('jx')-Js(1.0))).get(var.get('jy')))+(var.get('wy3')*var.get('zb').get((var.get('jx')-Js(1.0))).get((var.get('jy')+Js(1.0))))))
                                def PyJs_LONG_0_(var=var):
                                    return var.get('zxy').get(var.get('jx')).put(var.get('jy'), ((var.get('wy2')*((var.get('wx2')*var.get('zab').get((var.get('jx')-Js(1.0))).get((var.get('jy')-Js(1.0))))+(var.get('wx3')*var.get('zab').get(var.get('jx')).get((var.get('jy')-Js(1.0))))))+(var.get('wy3')*((var.get('wx2')*var.get('zab').get((var.get('jx')-Js(1.0))).get(var.get('jy')))+(var.get('wx3')*var.get('zab').get(var.get('jx')).get(var.get('jy')))))))
                                PyJs_LONG_0_()
                            finally:
                                    (var.put('jx',Js(var.get('jx').to_number())+Js(1))-Js(1))
                    finally:
                            (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                if (var.get('ix')==Js(0.0)):
                    var.put('w2', (var.get('a4')*((Js(3.0)*var.get('a3'))+var.get('a4'))))
                    var.put('w1', (((Js(2.0)*var.get('a3'))*(var.get('a3')-var.get('a4')))+var.get('w2')))
                    #for JS loop
                    var.put('jy', Js(1.0))
                    while (var.get('jy')<Js(3.0)):
                        try:
                            var.get('zx').get('0').put(var.get('jy'), (((var.get('w1')*var.get('za').get('0').get((var.get('jy')-Js(1.0))))+(var.get('w2')*var.get('za').get('1').get((var.get('jy')-Js(1.0)))))/(var.get('w1')+var.get('w2'))))
                            var.get('zy').get('0').put(var.get('jy'), ((Js(2.0)*var.get('zy').get('1').get(var.get('jy')))-var.get('zy').get('2').get(var.get('jy'))))
                            var.get('zxy').get('0').put(var.get('jy'), ((Js(2.0)*var.get('zxy').get('1').get(var.get('jy')))-var.get('zxy').get('2').get(var.get('jy'))))
                            #for JS loop
                            var.put('jx1', Js(1.0))
                            while (var.get('jx1')<Js(3.0)):
                                try:
                                    var.put('jx', (Js(3.0)-var.get('jx1')))
                                    var.get('zx').get(var.get('jx')).put(var.get('jy'), var.get('zx').get((var.get('jx')-Js(1.0))).get(var.get('jy')))
                                    var.get('zy').get(var.get('jx')).put(var.get('jy'), var.get('zy').get((var.get('jx')-Js(1.0))).get(var.get('jy')))
                                    var.get('zxy').get(var.get('jx')).put(var.get('jy'), var.get('zxy').get((var.get('jx')-Js(1.0))).get(var.get('jy')))
                                finally:
                                        (var.put('jx1',Js(var.get('jx1').to_number())+Js(1))-Js(1))
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                    var.put('x3', (Js(1.0)/var.get('a4')), '-')
                    var.put('z33', (var.get('za').get('1').get('0')/var.get('a4')), '-')
                    #for JS loop
                    var.put('jy', Js(0.0))
                    while (var.get('jy')<Js(5.0)):
                        try:
                            var.get('zb').get('1').put(var.get('jy'), var.get('zb').get('0').get(var.get('jy')))
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                    #for JS loop
                    var.put('jy', Js(1.0))
                    while (var.get('jy')<Js(4.0)):
                        try:
                            var.get('zb').get('0').put(var.get('jy'), (var.get('zab').get('0').get((var.get('jy')-Js(1.0)))/var.get('a4')), '-')
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                    var.put('a3', var.get('a4'))
                    var.get('za').get('2').put('0', var.get('za').get('1').get('0'))
                    #for JS loop
                    var.put('jy', Js(0.0))
                    while (var.get('jy')<Js(3.0)):
                        try:
                            var.get('zab').get('1').put(var.get('jy'), var.get('zab').get('0').get(var.get('jy')))
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                if (var.get('ix')==var.get('lx')):
                    var.put('w4', (var.get('a2')*((Js(3.0)*var.get('a3'))+var.get('a2'))))
                    var.put('w5', (((Js(2.0)*var.get('a3'))*(var.get('a3')-var.get('a2')))+var.get('w4')))
                    #for JS loop
                    var.put('jy', Js(1.0))
                    while (var.get('jy')<Js(3.0)):
                        try:
                            var.get('zx').get('3').put(var.get('jy'), (((var.get('w4')*var.get('za').get('3').get((var.get('jy')-Js(1.0))))+(var.get('w5')*var.get('za').get('4').get((var.get('jy')-Js(1.0)))))/(var.get('w4')+var.get('w5'))))
                            var.get('zy').get('3').put(var.get('jy'), ((Js(2.0)*var.get('zy').get('2').get(var.get('jy')))-var.get('zy').get('1').get(var.get('jy'))))
                            var.get('zxy').get('3').put(var.get('jy'), ((Js(2.0)*var.get('zxy').get('2').get(var.get('jy')))-var.get('zxy').get('1').get(var.get('jy'))))
                            #for JS loop
                            var.put('jx', Js(1.0))
                            while (var.get('jx')<Js(3.0)):
                                try:
                                    var.get('zx').get(var.get('jx')).put(var.get('jy'), var.get('zx').get((var.get('jx')+Js(1.0))).get(var.get('jy')))
                                    var.get('zy').get(var.get('jx')).put(var.get('jy'), var.get('zy').get((var.get('jx')+Js(1.0))).get(var.get('jy')))
                                    var.get('zxy').get(var.get('jx')).put(var.get('jy'), var.get('zxy').get((var.get('jx')+Js(1.0))).get(var.get('jy')))
                                finally:
                                        (var.put('jx',Js(var.get('jx').to_number())+Js(1))-Js(1))
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                    var.put('x3', var.get('x4'))
                    var.put('z33', var.get('z43'))
                    #for JS loop
                    var.put('jy', Js(0.0))
                    while (var.get('jy')<Js(5.0)):
                        try:
                            var.get('zb').get('0').put(var.get('jy'), var.get('zb').get('1').get(var.get('jy')))
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                    var.put('a3', var.get('a2'))
                    var.get('za').get('2').put('0', var.get('za').get('3').get('0'))
                    #for JS loop
                    var.put('jy', Js(0.0))
                    while (var.get('jy')<Js(3.0)):
                        try:
                            var.get('zab').get('1').put(var.get('jy'), var.get('zab').get('2').get(var.get('jy')))
                        finally:
                                (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                if (var.get('iy')==Js(0.0)):
                    var.put('w2', (var.get('b4')*((Js(3.0)*var.get('b3'))+var.get('b4'))))
                    var.put('w1', (((Js(2.0)*var.get('b3'))*(var.get('b3')-var.get('b4')))+var.get('w2')))
                    #for JS loop
                    var.put('jx', Js(1.0))
                    while (var.get('jx')<Js(3.0)):
                        try:
                            if (((var.get('ix')>Js(0.0)) or (var.get('jx')==Js(2.0))) and ((var.get('ix')<var.get('lx')) or (var.get('jx')==Js(1.0)))):
                                var.get('zy').get(var.get('jx')).put('0', (((var.get('w1')*var.get('zb').get((var.get('jx')-Js(1.0))).get('0'))+(var.get('w2')*var.get('zb').get((var.get('jx')-Js(1.0))).get('1')))/(var.get('w1')+var.get('w2'))))
                                var.get('zx').get(var.get('jx')).put('0', ((Js(2.0)*var.get('zx').get(var.get('jx')).get('1'))-var.get('zx').get(var.get('jx')).get('2')))
                                var.get('zxy').get(var.get('jx')).put('0', ((Js(2.0)*var.get('zxy').get(var.get('jx')).get('1'))-var.get('zxy').get(var.get('jx')).get('2')))
                            #for JS loop
                            var.put('jy1', Js(1.0))
                            while (var.get('jy1')<Js(3.0)):
                                try:
                                    var.put('jy', (Js(3.0)-var.get('jy1')))
                                    var.get('zy').get(var.get('jx')).put(var.get('jy'), var.get('zy').get(var.get('jx')).get((var.get('jy')-Js(1.0))))
                                    var.get('zx').get(var.get('jx')).put(var.get('jy'), var.get('zx').get(var.get('jx')).get((var.get('jy')-Js(1.0))))
                                    var.get('zxy').get(var.get('jx')).put(var.get('jy'), var.get('zxy').get(var.get('jx')).get((var.get('jy')-Js(1.0))))
                                finally:
                                        (var.put('jy1',Js(var.get('jy1').to_number())+Js(1))-Js(1))
                        finally:
                                (var.put('jx',Js(var.get('jx').to_number())+Js(1))-Js(1))
                    var.put('y3', (Js(1.0)/var.get('b4')), '-')
                    var.put('z33', (var.get('zb').get('0').get('1')/var.get('b4')), '-')
                    var.get('za').get('2').put('0', (var.get('zab').get('1').get('0')/var.get('b4')), '-')
                    var.get('zb').get('0').put('2', var.get('zb').get('0').get('1'))
                    var.get('zab').get('1').put('1', var.get('zab').get('1').get('0'))
                    var.put('b3', var.get('b4'))
                    if ((var.get('ix')==Js(0.0)) or (var.get('ix')==var.get('lx'))):
                        if (var.get('ix')==Js(0.0)):
                            var.put('jx', Js(1.0))
                            var.put('jx1', Js(2.0))
                        else:
                            var.put('jx', Js(2.0))
                            var.put('jx1', Js(1.0))
                        var.put('jx1', var.get('Math').callprop('floor', var.get('jx1')))
                        var.get('zx').get(var.get('jx')).put('1', ((var.get('zx').get(var.get('jx1')).get('1')+var.get('zx').get(var.get('jx')).get('2'))-var.get('zx').get(var.get('jx1')).get('2')))
                        var.get('zy').get(var.get('jx')).put('1', ((var.get('zy').get(var.get('jx1')).get('1')+var.get('zy').get(var.get('jx')).get('2'))-var.get('zy').get(var.get('jx1')).get('2')))
                        var.get('zxy').get(var.get('jx')).put('1', ((var.get('zxy').get(var.get('jx1')).get('1')+var.get('zxy').get(var.get('jx')).get('2'))-var.get('zxy').get(var.get('jx1')).get('2')))
                if (var.get('iy')==var.get('ly')):
                    var.put('w4', (var.get('b2')*((Js(3.0)*var.get('b3'))+var.get('b2'))))
                    var.put('w5', (((Js(2.0)*var.get('b3'))*(var.get('b3')-var.get('b2')))+var.get('w4')))
                    #for JS loop
                    var.put('jx', Js(1.0))
                    while (var.get('jx')<Js(3.0)):
                        try:
                            if (((var.get('ix')>Js(0.0)) or (var.get('jx')==Js(2.0))) and ((var.get('ix')<var.get('lx')) or (var.get('jx')==Js(1.0)))):
                                var.get('zy').get(var.get('jx')).put('3', (((var.get('w4')*var.get('zb').get((var.get('jx')-Js(1.0))).get('3'))+(var.get('w5')*var.get('zb').get((var.get('jx')-Js(1.0))).get('4')))/(var.get('w4')+var.get('w5'))))
                                var.get('zx').get(var.get('jx')).put('3', ((Js(2.0)*var.get('zx').get(var.get('jx')).get('2'))-var.get('zx').get(var.get('jx')).get('1')))
                                var.get('zxy').get(var.get('jx')).put('3', ((Js(2.0)*var.get('zxy').get(var.get('jx')).get('2'))-var.get('zxy').get(var.get('jx')).get('1')))
                            #for JS loop
                            var.put('jy', Js(1.0))
                            while (var.get('jy')<Js(3.0)):
                                try:
                                    var.get('zy').get(var.get('jx')).put(var.get('jy'), var.get('zy').get(var.get('jx')).get((var.get('jy')+Js(1.0))))
                                    var.get('zx').get(var.get('jx')).put(var.get('jy'), var.get('zx').get(var.get('jx')).get((var.get('jy')+Js(1.0))))
                                    var.get('zxy').get(var.get('jx')).put(var.get('jy'), var.get('zxy').get(var.get('jx')).get((var.get('jy')+Js(1.0))))
                                finally:
                                        (var.put('jy',Js(var.get('jy').to_number())+Js(1))-Js(1))
                        finally:
                                (var.put('jx',Js(var.get('jx').to_number())+Js(1))-Js(1))
                    var.put('y3', var.get('y4'))
                    var.put('z33', (var.get('zb').get('0').get('2')/var.get('b3')), '+')
                    var.get('za').get('2').put('0', (var.get('zab').get('1').get('1')/var.get('b3')), '+')
                    var.get('zb').get('0').put('2', var.get('zb').get('0').get('3'))
                    var.get('zab').get('1').put('1', var.get('zab').get('1').get('2'))
                    var.put('b3', var.get('b2'))
                    if ((var.get('ix')==Js(0.0)) or (var.get('ix')==var.get('lx'))):
                        if (var.get('ix')==Js(0.0)):
                            var.put('jx', Js(1.0))
                            var.put('jx1', Js(2.0))
                        else:
                            var.put('jx', Js(2.0))
                            var.put('jx1', Js(1.0))
                        var.get('zx').get(var.get('jx')).put('2', ((var.get('zx').get(var.get('jx1')).get('2')+var.get('zx').get(var.get('jx')).get('1'))-var.get('zx').get(var.get('jx1')).get('1')))
                        var.get('zy').get(var.get('jx')).put('2', ((var.get('zy').get(var.get('jx1')).get('2')+var.get('zy').get(var.get('jx')).get('1'))-var.get('zy').get(var.get('jx1')).get('1')))
                        var.get('zxy').get(var.get('jx')).put('2', ((var.get('zxy').get(var.get('jx1')).get('2')+var.get('zxy').get(var.get('jx')).get('1'))-var.get('zxy').get(var.get('jx1')).get('1')))
                var.put('zx3b3', ((var.get('zx').get('1').get('2')-var.get('zx').get('1').get('1'))*var.get('b3')))
                var.put('zx4b3', ((var.get('zx').get('2').get('2')-var.get('zx').get('2').get('1'))*var.get('b3')))
                var.put('zy3a3', ((var.get('zy').get('2').get('1')-var.get('zy').get('1').get('1'))*var.get('a3')))
                var.put('zy4a3', ((var.get('zy').get('2').get('2')-var.get('zy').get('1').get('2'))*var.get('a3')))
                var.put('a', (((var.get('zab').get('1').get('1')-var.get('zx3b3'))-var.get('zy3a3'))+var.get('zxy').get('1').get('1')))
                var.put('b', (((var.get('zx4b3')-var.get('zx3b3'))-var.get('zxy').get('2').get('1'))+var.get('zxy').get('1').get('1')))
                var.put('c', (((var.get('zy4a3')-var.get('zy3a3'))-var.get('zxy').get('1').get('2'))+var.get('zxy').get('1').get('1')))
                var.put('d', (((var.get('zxy').get('2').get('2')-var.get('zxy').get('2').get('1'))-var.get('zxy').get('1').get('2'))+var.get('zxy').get('1').get('1')))
                var.put('e', (((var.get('a')+var.get('a'))-var.get('b'))-var.get('c')))
                var.put('a3sq', (var.get('a3')*var.get('a3')))
                var.put('b3sq', (var.get('b3')*var.get('b3')))
                var.put('p02', ((((Js(2.0)*(var.get('zb').get('0').get('2')-var.get('zy').get('1').get('1')))+var.get('zb').get('0').get('2'))-var.get('zy').get('1').get('2'))*var.get('b3')))
                var.put('p03', (((((-Js(2.0))*var.get('zb').get('0').get('2'))+var.get('zy').get('1').get('2'))+var.get('zy').get('1').get('1'))*var.get('b3sq')))
                var.put('p12', ((((Js(2.0)*(var.get('zx3b3')-var.get('zxy').get('1').get('1')))+var.get('zx3b3'))-var.get('zxy').get('1').get('2'))*var.get('b3')))
                var.put('p13', (((((-Js(2.0))*var.get('zx3b3'))+var.get('zxy').get('1').get('2'))+var.get('zxy').get('1').get('1'))*var.get('b3sq')))
                var.put('p20', ((((Js(2.0)*(var.get('za').get('2').get('0')-var.get('zx').get('1').get('1')))+var.get('za').get('2').get('0'))-var.get('zx').get('2').get('1'))*var.get('a3')))
                var.put('p21', ((((Js(2.0)*(var.get('zy3a3')-var.get('zxy').get('1').get('1')))+var.get('zy3a3'))-var.get('zxy').get('2').get('1'))*var.get('a3')))
                var.put('p22', ((((Js(3.0)*(var.get('a')+var.get('e')))+var.get('d'))*var.get('a3'))*var.get('b3')))
                var.put('p23', ((((((-Js(3.0))*var.get('e'))-var.get('b'))-var.get('d'))*var.get('a3'))*var.get('b3sq')))
                var.put('p30', (((((-Js(2.0))*var.get('za').get('2').get('0'))+var.get('zx').get('2').get('1'))+var.get('zx').get('1').get('1'))*var.get('a3sq')))
                var.put('p31', (((((-Js(2.0))*var.get('zy3a3'))+var.get('zxy').get('2').get('1'))+var.get('zxy').get('1').get('1'))*var.get('a3sq')))
                var.put('p32', ((((((-Js(3.0))*var.get('e'))-var.get('c'))-var.get('d'))*var.get('b3'))*var.get('a3sq')))
                var.put('p33', ((((var.get('d')+var.get('e'))+var.get('e'))*var.get('a3sq'))*var.get('b3sq')))
            var.put('dy', (var.get('v').get(var.get('k'))-var.get('y3')))
            var.put('q0', (var.get('z33')+(var.get('dy')*(var.get('zy').get('1').get('1')+(var.get('dy')*(var.get('p02')+(var.get('dy')*var.get('p03'))))))))
            var.put('q1', (var.get('zx').get('1').get('1')+(var.get('dy')*(var.get('zxy').get('1').get('1')+(var.get('dy')*(var.get('p12')+(var.get('dy')*var.get('p13'))))))))
            var.put('q2', (var.get('p20')+(var.get('dy')*(var.get('p21')+(var.get('dy')*(var.get('p22')+(var.get('dy')*var.get('p23'))))))))
            var.put('q3', (var.get('p30')+(var.get('dy')*(var.get('p31')+(var.get('dy')*(var.get('p32')+(var.get('dy')*var.get('p33'))))))))
            var.put('dx', (var.get('u').get(var.get('k'))-var.get('x3')))
            var.get('w').put(var.get('k'), (var.get('q0')+(var.get('dx')*(var.get('q1')+(var.get('dx')*(var.get('q2')+(var.get('dx')*var.get('q3'))))))))
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
PyJsHoisted_itplbv_.func_name = 'itplbv'
var.put('itplbv', PyJsHoisted_itplbv_)
@Js
def PyJsHoisted_tvfmfs_metric_(erp, haat, channel, field, distance, fs_or_dist, curve, flag, this, arguments, var=var):
    var = Scope({'erp':erp, 'haat':haat, 'channel':channel, 'field':field, 'distance':distance, 'fs_or_dist':fs_or_dist, 'curve':curve, 'flag':flag, 'this':this, 'arguments':arguments}, var)
    var.registers(['curve', 'delta', 'd_first', 'fs_or_dist', 'id50', 'id10', 'L', 'f5010', 'RT', 'e_volts_meter', 'i', 'k', 'range', 'f1', 'f', 'd1', 'channel', 'field', 'n_points', 'erp', 'f5050', 'd_last', 'erp_db', 'RL', 'ih10', 'ih50', 'h', 'haat', 'T', 'sigma', 'distance', 'field_for_erp', 'flag', 'd', 'ZQ', 'j'])
    var.put('id50', Js(25.0))
    var.put('ih50', Js(13.0))
    var.put('id10', Js(31.0))
    var.put('ih10', Js(13.0))
    var.put('range', Js(100.0))
    var.put('delta', Js(0.5))
    var.put('erp_db', Js(0.0))
    var.put('d_first', Js(0.0))
    var.put('d_last', Js(0.0))
    var.put('e_volts_meter', Js(0.0))
    var.put('n_points', Js(1001.0))
    var.put('i', Js(0.0))
    var.put('j', Js(1.0))
    var.put('d', Js([]))
    var.put('h', Js([]))
    var.put('f', Js([]))
    var.put('f5050', Js([]))
    var.put('f5010', Js([]))
    var.put('L', Js(50.0))
    var.put('T', Js(90.0))
    var.put('ZQ', Js(0.0))
    var.put('sigma', Js(0.0))
    var.put('RL', Js(0.0))
    var.put('RT', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(19.0)):
        try:
            var.get('flag').put(var.get('i'), Js(0.0))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if ((((var.get('channel')<Js(2.0)) or (var.get('channel')>Js(300.0))) or ((var.get('channel')>Js(69.0)) and (var.get('channel')<Js(200.0)))) or (var.get('channel')==Js(''))):
        var.get('flag').put('3', Js(1.0))
    if (var.get('erp')<Js(0.0001)):
        var.get('flag').put('6', Js(1.0))
        if ((var.get('erp')<Js(0.0001)) and (var.get('erp')>Js(1e-08))):
            var.put('erp', Js(0.0001))
    if ((((var.get('channel')>=Js(2.0)) and (var.get('channel')<=Js(6.0))) or ((var.get('channel')>=Js(200.0)) and (var.get('channel')<=Js(300.0)))) and (var.get('erp')>Js(400.5))):
        var.get('flag').put('12', Js(1.0))
    else:
        if (((var.get('channel')>=Js(7.0)) and (var.get('channel')<=Js(13.0))) and (var.get('erp')>Js(400.5))):
            var.get('flag').put('13', Js(1.0))
        else:
            if (((var.get('channel')>=Js(14.0)) and (var.get('channel')<=Js(69.0))) and (var.get('erp')>Js(5500.5))):
                var.get('flag').put('14', Js(1.0))
    if (((var.get('curve')==Js(0.0)) or (var.get('curve')==Js(2.0))) and (var.get('distance')>Js(300.0))):
        var.get('flag').put('15', Js(1.0))
    else:
        if ((var.get('curve')==Js(1.0)) and (var.get('distance')>Js(500.0))):
            var.get('flag').put('16', Js(1.0))
    if (((var.get('curve')<Js(0.0)) or (var.get('curve')>Js(2.0))) or (var.get('curve')==Js(''))):
        var.get('flag').put('4', Js(1.0))
    if (((var.get('fs_or_dist')<Js(1.0)) or (var.get('fs_or_dist')>Js(3.0))) or (var.get('fs_or_dist')==Js(''))):
        var.get('flag').put('5', Js(1.0))
    if ((var.get('fs_or_dist')==Js(1.0)) and (var.get('field')<Js(0.0))):
        var.get('flag').put('9', Js(1.0))
        var.put('field', var.get('Math').callprop('abs', var.get('field')))
    if ((var.get('fs_or_dist')==Js(2.0)) and (var.get('distance')<Js(0.0))):
        var.get('flag').put('9', Js(1.0))
        var.put('distance', var.get('Math').callprop('abs', var.get('distance')))
    if (var.get('fs_or_dist')==Js(3.0)):
        var.put('field_for_erp', Js(60.0))
        var.put('erp', Js(1.0))
        if (var.get('channel')<Js(200.0)):
            var.get('flag').put('17', Js(1.0))
        var.put('curve', Js(0.0))
        var.put('channel', Js(250.0))
    var.put('erp_db', (Js(10.0)*(var.get('Math').callprop('log', var.get('erp'))/var.get('Math').callprop('log', Js(10.0)))))
    if (var.get('haat')<Js(30.0)):
        var.put('haat', Js(30.0))
        var.get('flag').put('7', Js(1.0))
    else:
        if (var.get('haat')>Js(1600.0)):
            var.put('haat', Js(1600.0))
            var.get('flag').put('8', Js(1.0))
    if (((var.get('flag').get('3')==Js(1.0)) or (var.get('flag').get('4')==Js(1.0))) or (var.get('flag').get('5')==Js(1.0))):
        return var.get('flag')
    else:
        if ((((((var.get('flag').get('12')==Js(1.0)) or (var.get('flag').get('13')==Js(1.0))) or (var.get('flag').get('14')==Js(1.0))) or (var.get('flag').get('15')==Js(1.0))) or (var.get('flag').get('16')==Js(1.0))) or (var.get('flag').get('17')==Js(1.0))):
            return var.get('flag')
    if ((var.get('fs_or_dist')==Js(1.0)) or (var.get('fs_or_dist')==Js(3.0))):
        var.put('n_points', Js(1.0))
        var.put('j', Js(1.0))
        if (var.get('distance')<Js(1.5)):
            var.put('field', ((Js(106.92)-(Js(20.0)*(var.get('Math').callprop('log', var.get('distance'))/var.get('Math').callprop('log', Js(10.0)))))+var.get('erp_db')))
            var.get('flag').put('1', Js(1.0))
            return var.get('field')
        if (((var.get('curve')==Js(0.0)) and (var.get('distance')>Js(300.0))) or ((var.get('curve')==Js(1.0)) and (var.get('distance')>Js(500.0)))):
            var.get('flag').put('2', Js(1.0))
        else:
            var.get('h').put('0', var.get('haat'))
            var.get('d').put('0', var.get('distance'))
            var.put('RL', Js(0.0))
            if (((var.get('channel')>=Js(2.0)) and (var.get('channel')<=Js(6.0))) or ((var.get('channel')>=Js(200.0)) and (var.get('channel')<=Js(300.0)))):
                if ((var.get('curve')==Js(0.0)) or ((var.get('curve')==Js(1.0)) and (var.get('distance')<Js(15.0)))):
                    var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                else:
                    if (var.get('curve')==Js(1.0)):
                        var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                    else:
                        if (var.get('curve')==Js(2.0)):
                            if (var.get('distance')>=Js(15.0)):
                                var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5010'))
                            else:
                                if (var.get('distance')<Js(15.0)):
                                    var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                    var.get('f5010').put('0', var.get('f5050').get('0'))
            else:
                if ((var.get('channel')>=Js(7.0)) and (var.get('channel')<=Js(13.0))):
                    if ((var.get('curve')==Js(0.0)) or ((var.get('curve')==Js(1.0)) and (var.get('distance')<Js(15.0)))):
                        var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                    else:
                        if (var.get('curve')==Js(1.0)):
                            var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                        else:
                            if (var.get('curve')==Js(2.0)):
                                if (var.get('distance')>=Js(15.0)):
                                    var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                    var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5010'))
                                else:
                                    if (var.get('distance')<Js(15.0)):
                                        var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                        var.get('f5010').put('0', var.get('f5050').get('0'))
                else:
                    if ((var.get('channel')>=Js(14.0)) and (var.get('channel')<=Js(69.0))):
                        if ((var.get('curve')==Js(0.0)) or ((var.get('curve')==Js(1.0)) and (var.get('distance')<Js(15.0)))):
                            var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55U'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                        else:
                            if (var.get('curve')==Js(1.0)):
                                var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51U'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                            else:
                                if (var.get('curve')==Js(2.0)):
                                    if (var.get('distance')>=Js(15.0)):
                                        var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55U'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                        var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51U'), var.get('j'), var.get('d'), var.get('h'), var.get('f5010'))
                                    else:
                                        if (var.get('distance')<Js(15.0)):
                                            var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55U'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                            var.get('f5010').put('0', var.get('f5050').get('0'))
        if (var.get('flag').get('1')==Js(1.0)):
            pass
        if ((var.get('curve')==Js(0.0)) or (var.get('curve')==Js(1.0))):
            var.put('field', (var.get('f').get('0')+var.get('erp_db')))
        else:
            if (var.get('curve')==Js(2.0)):
                var.put('ZQ', var.get('fzq')(var.get('T')))
                var.put('RT', ((var.get('f5010').get('0')-var.get('f5050').get('0'))*(var.get('ZQ')/Js(1.28155))))
                var.put('field', (((var.get('f5050').get('0')+var.get('RL'))+var.get('RT'))+var.get('erp_db')))
        if (var.get('fs_or_dist')==Js(3.0)):
            var.put('erp', var.get('Math').callprop('pow', Js(10.0), ((var.get('field_for_erp')-var.get('field'))/Js(10.0))))
            if (var.get('erp')>Js(100.0)):
                var.get('flag').put('10', Js(1.0))
            return var.get('erp')
        else:
            return var.get('field')
    else:
        if (var.get('fs_or_dist')==Js(2.0)):
            var.put('j', var.get('n_points'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<=var.get('n_points')):
                try:
                    var.get('h').put(var.get('i'), var.get('haat'))
                    var.get('f5050').put(var.get('i'), var.get('f5010').put(var.get('i'), var.get('f').put(var.get('i'), var.get('d').put(var.get('i'), Js(0.0)))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if ((var.get('curve')==Js(0.0)) or (var.get('curve')==Js(2.0))):
                var.put('d_first', Js(1.5))
                var.put('d_last', Js(300.0))
            else:
                if (var.get('curve')==Js(1.0)):
                    var.put('d_first', Js(15.0))
                    var.put('d_last', Js(500.0))
            var.put('k', var.get('Math').callprop('floor', (var.get('d_first')/var.get('delta'))))
            #for JS loop
            var.put('i', var.get('k'))
            while (var.get('i')<=var.get('n_points')):
                try:
                    var.get('d').put(var.get('i'), (var.get('i')*var.get('delta')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (((var.get('channel')>=Js(2.0)) and (var.get('channel')<=Js(6.0))) or ((var.get('channel')>=Js(200.0)) and (var.get('channel')<=Js(300.0)))):
                if (var.get('curve')==Js(0.0)):
                    var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                else:
                    if (var.get('curve')==Js(1.0)):
                        var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                    else:
                        if (var.get('curve')==Js(2.0)):
                            var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                            var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51LV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5010'))
            else:
                if ((var.get('channel')>=Js(7.0)) and (var.get('channel')<=Js(13.0))):
                    if (var.get('curve')==Js(0.0)):
                        var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                    else:
                        if (var.get('curve')==Js(1.0)):
                            var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                        else:
                            if (var.get('curve')==Js(2.0)):
                                var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51HV'), var.get('j'), var.get('d'), var.get('h'), var.get('f5010'))
                else:
                    if ((var.get('channel')>=Js(14.0)) and (var.get('channel')<=Js(69.0))):
                        if (var.get('curve')==Js(0.0)):
                            var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55U'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                        else:
                            if (var.get('curve')==Js(1.0)):
                                var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51U'), var.get('j'), var.get('d'), var.get('h'), var.get('f'))
                            else:
                                if (var.get('curve')==Js(2.0)):
                                    var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55U'), var.get('j'), var.get('d'), var.get('h'), var.get('f5050'))
                                    var.get('itplbv')(var.get('id10'), var.get('ih10'), var.get('D10'), var.get('H10'), var.get('F51U'), var.get('j'), var.get('d'), var.get('h'), var.get('f5010'))
            if ((var.get('curve')==Js(1.0)) or (var.get('curve')==Js(2.0))):
                var.put('d1', Js([]))
                var.put('f1', Js([]))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<Js(30.0)):
                    try:
                        var.get('f').put(var.get('i'), Js(0.0))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('n_points')):
                    try:
                        var.get('d1').put(var.get('i'), (var.get('i')*var.get('delta')))
                        var.get('f1').put(var.get('i'), Js(0.0))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (((var.get('channel')>=Js(2.0)) and (var.get('channel')<=Js(6.0))) or ((var.get('channel')>=Js(200.0)) and (var.get('channel')<=Js(300.0)))):
                    var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55LV'), var.get('j'), var.get('d1'), var.get('h'), var.get('f1'))
                else:
                    if ((var.get('channel')>=Js(7.0)) and (var.get('channel')<=Js(13.0))):
                        var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55HV'), var.get('j'), var.get('d1'), var.get('h'), var.get('f1'))
                    else:
                        if ((var.get('channel')>=Js(14.0)) and (var.get('channel')<=Js(69.0))):
                            var.get('itplbv')(var.get('id50'), var.get('ih50'), var.get('D50'), var.get('H50'), var.get('F55U'), var.get('j'), var.get('d1'), var.get('h'), var.get('f5050'))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<Js(30.0)):
                    try:
                        if (var.get('curve')==Js(1.0)):
                            var.get('f').put(var.get('i'), (var.get('f1').get(var.get('i'))*Js(1.0)))
                        else:
                            if (var.get('curve')==Js(2.0)):
                                var.get('f').put(var.get('i'), var.get('f5010').put(var.get('i'), (var.get('f5050').get(var.get('i'))*Js(1.0))))
                        var.get('d').put(var.get('i'), (var.get('i')*var.get('delta')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('i', Js(3.0))
            while (var.get('i')>Js(0.0)):
                try:
                    if (var.get('field')>var.get('f').get(var.get('i'))):
                        var.get('flag').put('1', Js(1.0))
                        var.put('e_volts_meter', (Js(1e-06)*var.get('Math').callprop('pow', Js(10.0), (var.get('field')/Js(20.0)))))
                        var.put('distance', ((Js(0.007014271)*var.get('Math').callprop('sqrt', (var.get('erp')*Js(1000.0))))/var.get('e_volts_meter')))
                        return var.get('distance')
                finally:
                        (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('n_points')):
                try:
                    if ((var.get('curve')==Js(0.0)) or (var.get('curve')==Js(1.0))):
                        var.get('f').put(var.get('i'), (var.get('f').get(var.get('i'))+var.get('erp_db')))
                    else:
                        if (var.get('curve')==Js(2.0)):
                            var.put('ZQ', var.get('fzq')(var.get('T')))
                            var.put('RT', ((var.get('f5010').get(var.get('i'))-var.get('f5050').get(var.get('i')))*(var.get('ZQ')/Js(1.28155))))
                            var.get('f').put(var.get('i'), (((var.get('f5050').get(var.get('i'))+var.get('RL'))+var.get('RT'))+var.get('erp_db')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('i', Js(1.0))
            while (var.get('i')<var.get('n_points')):
                try:
                    if ((var.get('field')>var.get('f').get(var.get('i'))) and (var.get('field')<var.get('f').get((var.get('i')-Js(1.0))))):
                        var.put('distance', ((((var.get('f').get((var.get('i')-Js(1.0)))-var.get('field'))/(var.get('f').get((var.get('i')-Js(1.0)))-var.get('f').get(var.get('i'))))*(var.get('d').get(var.get('i'))-var.get('d').get((var.get('i')-Js(1.0)))))+var.get('d').get((var.get('i')-Js(1.0)))))
                        if (var.get('distance')>var.get('d_last')):
                            var.get('flag').put('2', Js(1.0))
                        return var.get('distance')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_tvfmfs_metric_.func_name = 'tvfmfs_metric'
var.put('tvfmfs_metric', PyJsHoisted_tvfmfs_metric_)
@Js
def PyJsHoisted_tvfmfs_comment_(i, this, arguments, var=var):
    var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    if (var.get('i')==Js(0.0)):
        var.put('comment', Js(''))
    else:
        if (var.get('i')==Js(1.0)):
            var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Free Space equation used to compute distance.<br>\n '))
        else:
            if (var.get('i')==Js(2.0)):
                var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entered distance exceeds maximum curve distance.<br>\n'))
            else:
                if (var.get('i')==Js(3.0)):
                    var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select a channel range.<br>\n'))
                else:
                    if (var.get('i')==Js(4.0)):
                        var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select a contour type.<br>\n'))
                    else:
                        if (var.get('i')==Js(5.0)):
                            var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select the desired result (Find This).<br>\n'))
                        else:
                            if (var.get('i')==Js(6.0)):
                                var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ERP of less than 0.0001 kW (0.1 watt) is changed to 0.0001 kW for calculations.<br>\n'))
                            else:
                                if (var.get('i')==Js(7.0)):
                                    var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entered HAAT is less than 30 meters; changed to 30 meters for calculations.<br>\n'))
                                else:
                                    if (var.get('i')==Js(8.0)):
                                        var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entered HAAT is greater than 1600 meters; changed to 1600 meters for calculations.<br>\n'))
                                    else:
                                        if (var.get('i')==Js(9.0)):
                                            var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entered Field or Distance is less than zero; set to positive for calculations.<br>\n'))
                                        else:
                                            if (var.get('i')==Js(10.0)):
                                                var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ERP exceeds the maximum of 100 kW permitted for U.S. FM stations. <br>\n'))
                                            else:
                                                if (var.get('i')==Js(11.0)):
                                                    var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-numeric data entered in a form input. <br>\n'))
                                                else:
                                                    if (var.get('i')==Js(12.0)):
                                                        var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum ERP for VHF, TV Channels 2-6, is 400 kW. <br>\n'))
                                                    else:
                                                        if (var.get('i')==Js(13.0)):
                                                            var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum ERP for VHF, TV Channels 7-13, is 400 kW. <br>\n'))
                                                        else:
                                                            if (var.get('i')==Js(14.0)):
                                                                var.put('comment', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum ERP for UHF, TV Channels 14-69, is 5500 kW. <br>\n'))
                                                            else:
                                                                if (var.get('i')==Js(15.0)):
                                                                    var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum curve <b>distance</b> for service contours is limited to 300 km. <br>\n'))
                                                                else:
                                                                    if (var.get('i')==Js(16.0)):
                                                                        var.put('comment', Js('<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum curve <b>distance</b> for interfering contours is limited to 500 km.<br>\n'))
                                                                    else:
                                                                        if (var.get('i')==Js(17.0)):
                                                                            var.put('comment', Js("<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The 'Find ERP' calculation is not valid for the TV service.<br>\n"))
                                                                        else:
                                                                            var.put('comment', Js(''))
    return var.get('comment')
PyJsHoisted_tvfmfs_comment_.func_name = 'tvfmfs_comment'
var.put('tvfmfs_comment', PyJsHoisted_tvfmfs_comment_)
@Js
def PyJsHoisted_fzq_(Q, this, arguments, var=var):
    var = Scope({'Q':Q, 'this':this, 'arguments':arguments}, var)
    var.registers(['Q', 'k', 'ZGRID'])
    pass
    var.put('ZGRID', Js([]))
    var.put('ZQ', Js(0.0))
    #for JS loop
    var.put('k', Js(0.0))
    while (var.get('k')<=Js(57.0)):
        try:
            var.get('ZGRID').put(var.get('k'), (-var.get('ZGRI').get(var.get('k'))))
            var.get('ZGRID').put((Js(114.0)-var.get('k')), var.get('ZGRI').get(var.get('k')))
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('k', Js(1.0))
    while (var.get('k')<Js(115.0)):
        try:
            if (var.get('VGRID').get(var.get('k'))<var.get('Q')):
                pass
            else:
                var.put('ZQ', (var.get('ZGRID').get((var.get('k')-Js(1.0)))+(((var.get('Q')-var.get('VGRID').get((var.get('k')-Js(1.0))))/(var.get('VGRID').get(var.get('k'))-var.get('VGRID').get((var.get('k')-Js(1.0)))))*(var.get('ZGRID').get(var.get('k'))-var.get('ZGRID').get((var.get('k')-Js(1.0)))))))
                if PyJsStrictNeq(var.get('ZQ'),var.get('ZQ')):
                    var.put('ZQ', Js(0.0))
                return var.get('ZQ')
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
PyJsHoisted_fzq_.func_name = 'fzq'
var.put('fzq', PyJsHoisted_fzq_)
@Js
def PyJsHoisted_round_power_(power_in, error_flag, this, arguments, var=var):
    var = Scope({'power_in':power_in, 'error_flag':error_flag, 'this':this, 'arguments':arguments}, var)
    var.registers(['error_flag', 'round_factor', 'power_in', 'power_out'])
    var.put('power_out', Js(0.0))
    var.put('round_factor', Js(0.0))
    var.put('error_flag', Js(0.0))
    var.put('power_out', (var.get('power_in')+Js(1e-12)))
    if ((var.get('power_in')>=Js(0.001)) and (var.get('power_in')<Js(0.003))):
        var.put('round_factor', Js(5e-05))
    else:
        if ((var.get('power_in')>=Js(0.003)) and (var.get('power_in')<Js(0.01))):
            var.put('round_factor', Js(0.0001))
        else:
            if ((var.get('power_in')>=Js(0.01)) and (var.get('power_in')<Js(0.03))):
                var.put('round_factor', Js(0.0005))
            else:
                if ((var.get('power_in')>=Js(0.03)) and (var.get('power_in')<Js(0.1))):
                    var.put('round_factor', Js(0.001))
                else:
                    if ((var.get('power_in')>=Js(0.1)) and (var.get('power_in')<Js(0.3))):
                        var.put('round_factor', Js(0.005))
                    else:
                        if ((var.get('power_in')>=Js(0.3)) and (var.get('power_in')<Js(1.0))):
                            var.put('round_factor', Js(0.01))
                        else:
                            if ((var.get('power_in')>=Js(1.0)) and (var.get('power_in')<Js(3.0))):
                                var.put('round_factor', Js(0.05))
                            else:
                                if ((var.get('power_in')>=Js(3.0)) and (var.get('power_in')<Js(10.0))):
                                    var.put('round_factor', Js(0.1))
                                else:
                                    if ((var.get('power_in')>=Js(10.0)) and (var.get('power_in')<Js(30.0))):
                                        var.put('round_factor', Js(0.5))
                                    else:
                                        if ((var.get('power_in')>=Js(30.0)) and (var.get('power_in')<Js(100.0))):
                                            var.put('round_factor', Js(1.0))
                                        else:
                                            if ((var.get('power_in')>=Js(100.0)) and (var.get('power_in')<Js(300.0))):
                                                var.put('round_factor', Js(5.0))
                                            else:
                                                if ((var.get('power_in')>=Js(300.0)) and (var.get('power_in')<Js(1000.0))):
                                                    var.put('round_factor', Js(10.0))
    var.put('power_out', (var.get('power_in')/var.get('round_factor')))
    var.put('power_out', var.get('Math').callprop('floor', var.get('Math').callprop('round', var.get('power_out'))))
    var.put('power_out', (var.get('power_out')*var.get('round_factor')))
    if (var.get('power_in')>Js(1000.0)):
        var.put('power_out', var.get('Math').callprop('floor', var.get('power_in')))
    return var.get('power_out')
PyJsHoisted_round_power_.func_name = 'round_power'
var.put('round_power', PyJsHoisted_round_power_)
var.put('D50', Js([Js(1.609344), Js(3.218688), Js(4.828032), Js(6.437376), Js(8.04672), Js(16.09344), Js(32.18688), Js(48.28032), Js(64.37376), Js(80.4672), Js(96.56064), Js(112.65408), Js(128.74752), Js(144.84096), Js(160.9344), Js(177.02784), Js(193.12128), Js(209.21472), Js(225.30816), Js(241.4016), Js(257.49504), Js(273.58848), Js(289.68192), Js(305.77536), Js(321.8688), Js(0.0)]))
var.put('D10', Js([Js(16.09344), Js(32.18688), Js(48.28032), Js(64.37376), Js(80.4672), Js(96.56064), Js(112.65408), Js(128.74752), Js(144.84096), Js(160.9344), Js(177.02784), Js(193.12128), Js(209.21472), Js(225.30816), Js(241.4016), Js(257.49504), Js(273.58848), Js(289.68192), Js(305.77536), Js(321.8688), Js(337.96224), Js(354.05568), Js(370.14912), Js(386.24256), Js(402.336), Js(418.42944), Js(434.52288), Js(450.61632), Js(466.70976), Js(482.8032), Js(498.89644), Js(0.0)]))
var.put('H50', Js([Js(30.48), Js(60.96), Js(121.92), Js(182.88), Js(243.84), Js(304.8), Js(381.0), Js(457.2), Js(533.4), Js(609.6), Js(914.4), Js(1219.2), Js(1524.0), Js(0.0)]))
var.put('H10', Js([Js(30.48), Js(60.96), Js(121.92), Js(182.88), Js(243.84), Js(304.8), Js(381.0), Js(457.2), Js(533.4), Js(609.6), Js(914.4), Js(1219.2), Js(1524.0), Js(0.0)]))
var.put('F55LV', Js([Js(92.0), Js(79.7), Js(72.7), Js(67.8), Js(64.0), Js(52.0), Js(39.4), Js(31.0), Js(25.3), Js(20.3), Js(16.2), Js(12.8), Js(9.8), Js(6.9), Js(4.0), Js(1.5), (-Js(1.1)), (-Js(3.6)), (-Js(5.8)), (-Js(8.1)), (-Js(10.6)), (-Js(13.0)), (-Js(15.1)), (-Js(17.2)), (-Js(19.2)), Js(98.0), Js(85.9), Js(79.0), Js(73.8), Js(70.0), Js(58.0), Js(45.5), Js(37.0), Js(29.5), Js(23.5), Js(18.1), Js(14.5), Js(11.0), Js(8.2), Js(5.5), Js(2.9), Js(0.3), (-Js(2.2)), (-Js(4.8)), (-Js(7.0)), (-Js(9.4)), (-Js(11.7)), (-Js(14.0)), (-Js(16.1)), (-Js(18.3)), Js(100.6), Js(91.0), Js(84.8), Js(80.0), Js(76.0), Js(64.0), Js(51.5), Js(43.0), Js(35.5), Js(28.8), Js(22.0), Js(17.1), Js(13.4), Js(10.2), Js(7.4), Js(4.8), Js(2.2), (-Js(0.3)), (-Js(3.0)), (-Js(5.2)), (-Js(7.6)), (-Js(10.0)), (-Js(12.2)), (-Js(14.6)), (-Js(16.9)), Js(101.5), Js(93.4), Js(87.8), Js(83.3), Js(79.6), Js(67.6), Js(55.0), Js(46.7), Js(39.0), Js(32.0), Js(25.3), Js(19.8), Js(15.2), Js(11.8), Js(8.9), Js(6.0), Js(3.7), Js(1.0), (-Js(1.4)), (-Js(3.9)), (-Js(6.1)), (-Js(8.7)), (-Js(11.0)), (-Js(13.2)), (-Js(15.6)), Js(101.9), Js(94.6), Js(89.4), Js(85.4), Js(82.0), Js(70.0), Js(57.6), Js(49.0), Js(41.5), Js(34.4), Js(27.7), Js(22.0), Js(17.0), Js(13.1), Js(10.1), Js(7.2), Js(4.8), Js(2.0), (-Js(0.3)), (-Js(2.7)), (-Js(5.1)), (-Js(7.6)), (-Js(10.0)), (-Js(12.1)), (-Js(14.6)), Js(102.0), Js(95.0), Js(90.4), Js(86.8), Js(83.7), Js(72.0), Js(59.6), Js(51.0), Js(43.6), Js(36.7), Js(29.9), Js(23.9), Js(18.8), Js(14.7), Js(11.5), Js(8.4), Js(5.7), Js(3.0), Js(0.6), (-Js(1.8)), (-Js(4.2)), (-Js(6.6)), (-Js(9.0)), (-Js(11.2)), (-Js(13.6)), Js(102.1), Js(95.6), Js(91.2), Js(87.7), Js(85.0), Js(73.9), Js(61.7), Js(53.2), Js(45.9), Js(39.1), Js(32.0), Js(26.0), Js(21.0), Js(16.8), Js(13.1), Js(9.9), Js(7.0), Js(4.1), Js(1.7), (-Js(0.7)), (-Js(3.2)), (-Js(5.6)), (-Js(8.0)), (-Js(10.2)), (-Js(12.5)), Js(102.2), Js(95.9), Js(91.8), Js(88.3), Js(85.8), Js(75.4), Js(63.3), Js(55.1), Js(47.9), Js(41.5), Js(34.4), Js(28.3), Js(23.2), Js(18.8), Js(14.9), Js(11.1), Js(8.0), Js(5.2), Js(2.7), Js(0.2), (-Js(2.2)), (-Js(4.6)), (-Js(7.0)), (-Js(9.2)), (-Js(11.6)), Js(102.3), Js(96.0), Js(92.0), Js(88.9), Js(86.3), Js(76.7), Js(64.9), Js(57.0), Js(50.0), Js(43.5), Js(36.7), Js(30.7), Js(25.2), Js(20.4), Js(16.0), Js(12.5), Js(9.1), Js(6.2), Js(3.8), Js(1.1), (-Js(1.3)), (-Js(3.6)), (-Js(6.1)), (-Js(8.4)), (-Js(10.6)), Js(102.4), Js(96.1), Js(92.2), Js(89.2), Js(86.7), Js(77.9), Js(66.2), Js(58.5), Js(51.5), Js(45.0), Js(38.2), Js(32.4), Js(27.0), Js(22.0), Js(17.3), Js(13.7), Js(10.1), Js(7.1), Js(4.6), Js(2.0), (-Js(0.4)), (-Js(2.7)), (-Js(5.1)), (-Js(7.6)), (-Js(10.0)), Js(102.5), Js(96.3), Js(92.5), Js(89.9), Js(87.6), Js(80.2), Js(70.0), Js(62.6), Js(55.4), Js(48.9), Js(42.5), Js(36.9), Js(31.0), Js(25.7), Js(21.0), Js(17.1), Js(13.6), Js(10.3), Js(7.8), Js(5.1), Js(2.8), Js(0.5), (-Js(2.1)), (-Js(4.5)), (-Js(6.8)), Js(102.5), Js(96.5), Js(92.5), Js(90.1), Js(88.0), Js(81.3), Js(72.4), Js(65.0), Js(57.8), Js(51.2), Js(44.9), Js(39.1), Js(33.2), Js(28.1), Js(23.5), Js(19.8), Js(16.1), Js(13.0), Js(10.4), Js(8.0), Js(5.5), Js(3.1), Js(0.6), (-Js(2.0)), (-Js(4.1)), Js(102.5), Js(96.5), Js(92.5), Js(90.2), Js(88.1), Js(81.9), Js(74.2), Js(66.5), Js(59.6), Js(53.0), Js(46.4), Js(40.8), Js(35.0), Js(30.0), Js(25.5), Js(21.8), Js(18.3), Js(15.0), Js(12.4), Js(10.0), Js(7.7), Js(5.1), Js(2.8), Js(0.2), (-Js(2.0))]))
var.put('F51LV', Js([Js(52.2), Js(41.4), Js(36.4), Js(33.0), Js(30.0), Js(26.7), Js(23.5), Js(20.4), Js(17.4), Js(14.5), Js(11.5), Js(8.5), Js(5.9), Js(3.0), Js(0.6), (-Js(2.0)), (-Js(4.3)), (-Js(6.6)), (-Js(8.7)), (-Js(10.5)), (-Js(12.5)), (-Js(14.6)), (-Js(16.6)), (-Js(18.6)), (-Js(20.5)), (-Js(22.4)), (-Js(24.3)), (-Js(26.2)), (-Js(28.1)), (-Js(30.0)), (-Js(31.9)), Js(58.4), Js(47.0), Js(40.9), Js(36.0), Js(31.9), Js(28.0), Js(24.9), Js(22.0), Js(19.0), Js(16.1), Js(13.1), Js(10.1), Js(7.7), Js(4.9), Js(2.0), (-Js(0.4)), (-Js(3.0)), (-Js(5.1)), (-Js(7.4)), (-Js(9.4)), (-Js(11.4)), (-Js(13.4)), (-Js(15.5)), (-Js(17.4)), (-Js(19.3)), (-Js(21.2)), (-Js(23.2)), (-Js(25.0)), (-Js(27.0)), (-Js(29.0)), (-Js(31.0)), Js(64.3), Js(53.0), Js(45.9), Js(39.9), Js(35.0), Js(30.5), Js(26.9), Js(24.0), Js(20.9), Js(18.2), Js(15.3), Js(12.4), Js(9.8), Js(6.9), Js(4.1), Js(1.6), (-Js(1.0)), (-Js(3.4)), (-Js(5.8)), (-Js(8.0)), (-Js(10.1)), (-Js(12.0)), (-Js(14.1)), (-Js(16.0)), (-Js(18.0)), (-Js(19.9)), (-Js(21.9)), (-Js(23.7)), (-Js(25.6)), (-Js(27.4)), (-Js(29.2)), Js(68.0), Js(56.5), Js(49.0), Js(43.0), Js(37.7), Js(32.8), Js(28.8), Js(25.6), Js(22.5), Js(19.8), Js(16.9), Js(13.9), Js(11.0), Js(8.2), Js(5.7), Js(2.9), Js(0.3), (-Js(2.2)), (-Js(4.6)), (-Js(6.9)), (-Js(9.0)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(17.0)), (-Js(18.9)), (-Js(20.9)), (-Js(22.5)), (-Js(24.6)), (-Js(26.3)), (-Js(28.0)), Js(70.5), Js(59.0), Js(51.7), Js(45.4), Js(40.0), Js(34.9), Js(30.4), Js(27.0), Js(23.9), Js(21.0), Js(18.2), Js(15.1), Js(12.3), Js(9.7), Js(6.9), Js(4.1), Js(1.6), (-Js(1.0)), (-Js(3.4)), (-Js(5.7)), (-Js(8.0)), (-Js(10.0)), (-Js(12.0)), (-Js(14.0)), (-Js(16.0)), (-Js(17.9)), (-Js(19.9)), (-Js(21.7)), (-Js(23.6)), (-Js(25.4)), (-Js(27.2)), Js(72.3), Js(60.9), Js(53.7), Js(47.5), Js(41.9), Js(36.8), Js(32.0), Js(28.4), Js(25.0), Js(22.0), Js(19.2), Js(16.2), Js(13.4), Js(10.7), Js(8.0), Js(5.3), Js(2.7), Js(0.0), (-Js(2.5)), (-Js(4.9)), (-Js(7.0)), (-Js(9.0)), (-Js(11.2)), (-Js(13.2)), (-Js(15.1)), (-Js(17.0)), (-Js(19.0)), (-Js(21.0)), (-Js(23.0)), (-Js(24.6)), (-Js(26.2)), Js(74.2), Js(63.0), Js(56.0), Js(50.0), Js(44.4), Js(39.2), Js(34.9), Js(30.8), Js(27.0), Js(23.9), Js(20.8), Js(17.8), Js(14.8), Js(12.0), Js(9.1), Js(6.7), Js(3.9), Js(1.1), (-Js(1.4)), (-Js(3.9)), (-Js(6.0)), (-Js(8.0)), (-Js(10.2)), (-Js(12.2)), (-Js(14.2)), (-Js(16.2)), (-Js(18.1)), (-Js(20.0)), (-Js(22.0)), (-Js(23.7)), (-Js(25.4)), Js(75.9), Js(64.8), Js(57.9), Js(52.0), Js(46.7), Js(41.6), Js(37.1), Js(33.0), Js(29.0), Js(25.5), Js(22.0), Js(19.0), Js(16.0), Js(13.2), Js(10.3), Js(7.9), Js(5.0), Js(2.2), (-Js(0.2)), (-Js(2.8)), (-Js(5.0)), (-Js(7.0)), (-Js(9.2)), (-Js(11.3)), (-Js(13.3)), (-Js(15.3)), (-Js(17.2)), (-Js(19.2)), (-Js(21.1)), (-Js(22.8)), (-Js(24.5)), Js(77.0), Js(66.2), Js(59.6), Js(54.0), Js(48.5), Js(43.5), Js(39.2), Js(35.0), Js(30.8), Js(26.9), Js(23.2), Js(20.0), Js(17.1), Js(14.2), Js(11.6), Js(9.0), Js(6.0), Js(3.3), Js(0.9), (-Js(1.8)), (-Js(4.0)), (-Js(6.2)), (-Js(8.2)), (-Js(10.5)), (-Js(12.5)), (-Js(14.6)), (-Js(16.3)), (-Js(18.4)), (-Js(20.2)), (-Js(22.0)), (-Js(23.8)), Js(78.2), Js(67.6), Js(60.9), Js(55.2), Js(50.0), Js(45.0), Js(40.7), Js(36.2), Js(32.0), Js(28.0), Js(24.1), Js(21.0), Js(18.0), Js(15.3), Js(12.5), Js(10.0), Js(7.0), Js(4.4), Js(1.8), (-Js(0.8)), (-Js(3.0)), (-Js(5.3)), (-Js(7.4)), (-Js(9.8)), (-Js(11.8)), (-Js(14.0)), (-Js(15.8)), (-Js(17.8)), (-Js(19.6)), (-Js(21.3)), (-Js(23.0)), Js(80.8), Js(71.2), Js(64.5), Js(58.9), Js(53.9), Js(49.0), Js(44.2), Js(39.8), Js(35.4), Js(31.3), Js(27.6), Js(24.4), Js(21.6), Js(18.9), Js(16.0), Js(13.6), Js(10.7), Js(8.0), Js(5.2), Js(2.8), Js(0.3), (-Js(2.0)), (-Js(4.5)), (-Js(7.0)), (-Js(9.0)), (-Js(11.1)), (-Js(13.2)), (-Js(15.0)), (-Js(17.0)), (-Js(19.0)), (-Js(21.0)), Js(81.8), Js(73.8), Js(67.0), Js(61.4), Js(56.3), Js(51.7), Js(46.9), Js(42.0), Js(37.8), Js(33.8), Js(30.0), Js(27.0), Js(24.1), Js(21.5), Js(18.8), Js(16.1), Js(13.6), Js(10.9), Js(8.1), Js(5.3), Js(3.0), Js(0.4), (-Js(1.9)), (-Js(4.3)), (-Js(6.7)), (-Js(9.0)), (-Js(11.0)), (-Js(12.9)), (-Js(14.9)), (-Js(16.9)), (-Js(18.9)), Js(82.2), Js(75.5), Js(69.0), Js(63.3), Js(58.4), Js(53.5), Js(48.8), Js(44.0), Js(39.7), Js(35.7), Js(32.1), Js(29.1), Js(26.1), Js(23.5), Js(20.9), Js(18.0), Js(15.7), Js(13.0), Js(10.2), Js(7.5), Js(5.0), Js(2.6), Js(0.0), (-Js(2.4)), (-Js(4.6)), (-Js(6.9)), (-Js(9.0)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(17.0))]))
var.put('F55HV', Js([Js(94.6), Js(82.8), Js(75.7), Js(70.7), Js(66.8), Js(55.0), Js(42.5), Js(34.0), Js(26.3), Js(20.7), Js(16.3), Js(12.9), Js(9.9), Js(7.0), Js(4.3), Js(1.5), (-Js(1.0)), (-Js(3.5)), (-Js(5.7)), (-Js(8.0)), (-Js(10.4)), (-Js(12.8)), (-Js(15.0)), (-Js(17.2)), (-Js(19.1)), Js(100.7), Js(88.9), Js(81.8), Js(76.9), Js(73.0), Js(61.0), Js(48.6), Js(40.0), Js(32.0), Js(24.1), Js(18.5), Js(14.4), Js(11.2), Js(8.3), Js(5.5), Js(2.9), Js(0.5), (-Js(2.0)), (-Js(4.3)), (-Js(6.9)), (-Js(9.2)), (-Js(11.5)), (-Js(13.8)), (-Js(16.0)), (-Js(18.2)), Js(101.6), Js(92.3), Js(86.6), Js(82.2), Js(78.8), Js(67.2), Js(54.7), Js(46.1), Js(38.1), Js(30.1), Js(23.0), Js(17.0), Js(13.5), Js(10.5), Js(7.5), Js(4.8), Js(2.3), (-Js(0.3)), (-Js(2.7)), (-Js(5.0)), (-Js(7.3)), (-Js(9.8)), (-Js(12.0)), (-Js(14.4)), (-Js(16.8)), Js(101.8), Js(93.9), Js(88.7), Js(84.8), Js(81.6), Js(70.8), Js(58.1), Js(49.8), Js(41.7), Js(33.8), Js(26.2), Js(20.0), Js(15.2), Js(12.0), Js(9.0), Js(6.2), Js(3.7), Js(1.0), (-Js(1.2)), (-Js(3.7)), (-Js(6.0)), (-Js(8.4)), (-Js(10.7)), (-Js(13.0)), (-Js(15.5)), Js(101.9), Js(94.6), Js(89.8), Js(86.2), Js(83.2), Js(73.2), Js(60.7), Js(52.1), Js(44.0), Js(36.1), Js(28.8), Js(22.1), Js(17.0), Js(13.7), Js(10.4), Js(7.5), Js(4.8), Js(2.2), (-Js(0.1)), (-Js(2.5)), (-Js(4.9)), (-Js(7.3)), (-Js(9.7)), (-Js(12.0)), (-Js(14.4)), Js(102.0), Js(95.0), Js(90.5), Js(87.0), Js(84.5), Js(75.0), Js(62.5), Js(54.2), Js(46.0), Js(38.0), Js(30.6), Js(24.0), Js(18.9), Js(15.0), Js(11.5), Js(8.6), Js(5.8), Js(3.2), Js(0.9), (-Js(1.5)), (-Js(4.0)), (-Js(6.3)), (-Js(8.7)), (-Js(11.0)), (-Js(13.4)), Js(102.3), Js(95.4), Js(91.3), Js(88.0), Js(85.7), Js(77.0), Js(65.0), Js(56.7), Js(48.8), Js(40.9), Js(33.5), Js(26.8), Js(21.2), Js(17.0), Js(13.1), Js(10.0), Js(7.0), Js(4.4), Js(2.0), (-Js(0.5)), (-Js(3.0)), (-Js(5.3)), (-Js(7.6)), (-Js(10.0)), (-Js(12.3)), Js(102.3), Js(95.7), Js(91.8), Js(88.7), Js(86.3), Js(78.1), Js(67.6), Js(59.0), Js(51.0), Js(43.5), Js(36.3), Js(29.6), Js(23.9), Js(19.0), Js(14.9), Js(11.2), Js(8.2), Js(5.5), Js(3.0), Js(0.6), (-Js(2.0)), (-Js(4.3)), (-Js(6.6)), (-Js(9.0)), (-Js(11.3)), Js(102.3), Js(95.9), Js(92.0), Js(89.1), Js(87.0), Js(79.1), Js(69.5), Js(61.0), Js(53.3), Js(46.0), Js(39.0), Js(32.0), Js(26.0), Js(21.0), Js(16.2), Js(12.7), Js(9.5), Js(6.5), Js(4.0), Js(1.5), (-Js(1.0)), (-Js(3.5)), (-Js(5.8)), (-Js(8.2)), (-Js(10.5)), Js(102.4), Js(96.0), Js(92.1), Js(89.5), Js(87.3), Js(80.0), Js(71.0), Js(62.8), Js(55.0), Js(47.9), Js(41.0), Js(34.0), Js(28.0), Js(22.6), Js(17.5), Js(13.6), Js(10.5), Js(7.4), Js(4.9), Js(2.2), (-Js(0.2)), (-Js(2.6)), (-Js(5.0)), (-Js(7.3)), (-Js(9.8)), Js(102.4), Js(96.2), Js(92.6), Js(90.0), Js(88.0), Js(81.1), Js(73.9), Js(66.3), Js(58.7), Js(52.0), Js(45.0), Js(38.2), Js(32.0), Js(26.3), Js(21.1), Js(17.0), Js(14.0), Js(10.7), Js(8.0), Js(5.6), Js(3.0), Js(0.6), (-Js(1.8)), (-Js(4.2)), (-Js(6.6)), Js(102.4), Js(96.2), Js(92.6), Js(90.0), Js(88.0), Js(81.8), Js(74.8), Js(67.4), Js(60.3), Js(53.8), Js(47.0), Js(40.6), Js(34.4), Js(28.8), Js(23.8), Js(19.8), Js(16.6), Js(13.1), Js(10.4), Js(8.2), Js(5.5), Js(3.1), Js(0.9), (-Js(1.8)), (-Js(4.0)), Js(102.5), Js(96.5), Js(92.7), Js(90.1), Js(88.0), Js(82.0), Js(75.0), Js(68.0), Js(61.1), Js(54.6), Js(48.1), Js(42.0), Js(36.1), Js(30.6), Js(25.5), Js(21.8), Js(18.5), Js(15.1), Js(12.3), Js(10.1), Js(7.5), Js(5.1), Js(2.9), Js(0.3), (-Js(1.9))]))
var.put('F51HV', Js([Js(55.4), Js(44.4), Js(39.2), Js(34.0), Js(29.9), Js(26.6), Js(23.5), Js(20.3), Js(17.4), Js(14.3), Js(11.3), Js(8.6), Js(5.8), Js(2.9), Js(0.3), (-Js(2.1)), (-Js(4.4)), (-Js(6.7)), (-Js(8.9)), (-Js(10.8)), (-Js(12.9)), (-Js(14.8)), (-Js(16.9)), (-Js(18.8)), (-Js(20.7)), (-Js(22.7)), (-Js(24.6)), (-Js(26.4)), (-Js(28.2)), (-Js(30.1)), (-Js(32.0)), Js(61.6), Js(50.0), Js(43.5), Js(38.0), Js(32.5), Js(28.2), Js(25.0), Js(22.0), Js(19.0), Js(16.0), Js(13.0), Js(10.0), Js(7.2), Js(4.7), Js(1.9), (-Js(0.7)), (-Js(3.2)), (-Js(5.4)), (-Js(7.8)), (-Js(9.8)), (-Js(11.8)), (-Js(13.8)), (-Js(15.8)), (-Js(17.7)), (-Js(19.7)), (-Js(21.4)), (-Js(23.3)), (-Js(25.2)), (-Js(27.1)), (-Js(29.0)), (-Js(30.9)), Js(67.7), Js(55.8), Js(48.6), Js(42.7), Js(35.9), Js(31.0), Js(27.0), Js(24.0), Js(21.0), Js(18.1), Js(15.1), Js(12.2), Js(9.4), Js(6.8), Js(3.8), Js(1.2), (-Js(1.4)), (-Js(3.8)), (-Js(6.1)), (-Js(8.2)), (-Js(10.3)), (-Js(12.3)), (-Js(14.3)), (-Js(16.3)), (-Js(18.3)), (-Js(20.1)), (-Js(22.0)), (-Js(24.0)), (-Js(25.9)), (-Js(27.7)), (-Js(29.5)), Js(71.0), Js(59.1), Js(52.0), Js(45.6), Js(38.8), Js(33.4), Js(28.9), Js(25.5), Js(22.4), Js(19.6), Js(16.7), Js(13.7), Js(10.8), Js(8.1), Js(5.2), Js(2.7), Js(0.0), (-Js(2.3)), (-Js(4.8)), (-Js(7.0)), (-Js(9.0)), (-Js(11.1)), (-Js(13.1)), (-Js(15.1)), (-Js(17.0)), (-Js(19.0)), (-Js(20.9)), (-Js(22.9)), (-Js(24.8)), (-Js(26.5)), (-Js(28.2)), Js(73.5), Js(61.7), Js(54.6), Js(48.0), Js(41.0), Js(35.4), Js(30.7), Js(27.0), Js(23.8), Js(20.8), Js(18.0), Js(15.0), Js(12.0), Js(9.5), Js(6.5), Js(3.9), Js(1.2), (-Js(1.2)), (-Js(3.8)), (-Js(6.0)), (-Js(8.2)), (-Js(10.2)), (-Js(12.2)), (-Js(14.2)), (-Js(16.2)), (-Js(18.0)), (-Js(20.0)), (-Js(21.9)), (-Js(23.9)), (-Js(25.5)), (-Js(27.1)), Js(75.3), Js(63.7), Js(56.5), Js(50.0), Js(43.0), Js(37.4), Js(32.3), Js(28.3), Js(25.0), Js(22.0), Js(19.1), Js(16.3), Js(13.3), Js(10.6), Js(7.8), Js(5.0), Js(2.4), Js(0.0), (-Js(2.6)), (-Js(5.0)), (-Js(7.1)), (-Js(9.3)), (-Js(11.2)), (-Js(13.3)), (-Js(15.3)), (-Js(17.2)), (-Js(19.1)), (-Js(21.0)), (-Js(23.0)), (-Js(24.9)), (-Js(26.7)), Js(77.1), Js(66.5), Js(59.0), Js(52.5), Js(45.8), Js(40.0), Js(35.0), Js(30.4), Js(26.9), Js(23.5), Js(20.5), Js(17.6), Js(14.7), Js(12.0), Js(9.0), Js(6.4), Js(3.7), Js(1.0), (-Js(1.4)), (-Js(4.0)), (-Js(6.0)), (-Js(8.2)), (-Js(10.2)), (-Js(12.3)), (-Js(14.3)), (-Js(16.2)), (-Js(18.2)), (-Js(20.0)), (-Js(22.0)), (-Js(23.9)), (-Js(25.8)), Js(78.6), Js(68.9), Js(61.5), Js(54.9), Js(48.2), Js(43.0), Js(37.4), Js(32.9), Js(28.8), Js(25.0), Js(22.0), Js(18.8), Js(15.9), Js(13.0), Js(10.3), Js(7.5), Js(4.9), Js(2.1), (-Js(0.3)), (-Js(3.0)), (-Js(5.1)), (-Js(7.4)), (-Js(9.4)), (-Js(11.4)), (-Js(13.5)), (-Js(15.4)), (-Js(17.4)), (-Js(19.2)), (-Js(21.1)), (-Js(23.0)), (-Js(24.9)), Js(79.6), Js(70.8), Js(63.6), Js(56.9), Js(50.8), Js(45.4), Js(40.0), Js(35.0), Js(30.4), Js(26.4), Js(23.0), Js(19.9), Js(17.0), Js(14.1), Js(11.5), Js(8.8), Js(6.0), Js(3.3), Js(0.8), (-Js(2.0)), (-Js(4.2)), (-Js(6.5)), (-Js(8.6)), (-Js(10.6)), (-Js(12.8)), (-Js(14.8)), (-Js(16.8)), (-Js(18.5)), (-Js(20.3)), (-Js(22.1)), (-Js(23.9)), Js(80.4), Js(72.0), Js(65.2), Js(58.8), Js(53.0), Js(47.6), Js(42.0), Js(36.8), Js(32.0), Js(27.7), Js(24.0), Js(20.7), Js(18.0), Js(15.2), Js(12.5), Js(9.8), Js(7.0), Js(4.3), Js(1.7), (-Js(1.0)), (-Js(3.3)), (-Js(5.6)), (-Js(7.8)), (-Js(9.8)), (-Js(12.0)), (-Js(14.0)), (-Js(16.0)), (-Js(18.0)), (-Js(19.6)), (-Js(21.5)), (-Js(23.4)), Js(82.0), Js(75.0), Js(68.6), Js(62.5), Js(57.0), Js(52.0), Js(46.8), Js(41.5), Js(35.8), Js(31.0), Js(27.6), Js(24.0), Js(21.4), Js(18.8), Js(16.0), Js(13.1), Js(10.6), Js(7.9), Js(5.0), Js(2.5), Js(0.0), (-Js(2.4)), (-Js(4.7)), (-Js(6.9)), (-Js(9.0)), (-Js(11.1)), (-Js(13.1)), (-Js(15.1)), (-Js(17.0)), (-Js(19.0)), (-Js(21.0)), Js(82.4), Js(75.9), Js(69.8), Js(64.0), Js(58.9), Js(53.8), Js(48.9), Js(43.7), Js(38.2), Js(33.6), Js(30.0), Js(26.8), Js(24.0), Js(21.2), Js(18.7), Js(15.9), Js(13.2), Js(10.6), Js(8.0), Js(5.2), Js(2.8), Js(0.2), (-Js(2.0)), (-Js(4.3)), (-Js(6.5)), (-Js(9.0)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(16.8)), (-Js(18.6)), Js(82.5), Js(76.2), Js(70.2), Js(64.9), Js(59.8), Js(54.8), Js(50.0), Js(45.0), Js(40.1), Js(35.5), Js(32.0), Js(28.9), Js(26.0), Js(23.4), Js(20.7), Js(18.0), Js(15.4), Js(12.8), Js(10.0), Js(7.3), Js(4.9), Js(2.2), (-Js(0.1)), (-Js(2.4)), (-Js(4.7)), (-Js(7.0)), (-Js(9.0)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(17.0))]))
var.put('F55U', Js([Js(92.0), Js(80.0), Js(72.9), Js(67.9), Js(63.8), Js(51.9), Js(39.0), Js(27.5), Js(17.8), Js(13.0), Js(10.1), Js(7.0), Js(4.2), Js(1.6), (-Js(1.0)), (-Js(3.2)), (-Js(5.0)), (-Js(7.2)), (-Js(9.1)), (-Js(11.0)), (-Js(13.1)), (-Js(15.1)), (-Js(17.2)), (-Js(19.3)), (-Js(21.4)), Js(97.9), Js(86.0), Js(79.0), Js(74.0), Js(70.0), Js(58.0), Js(45.2), Js(33.5), Js(22.7), Js(16.0), Js(11.7), Js(8.5), Js(5.5), Js(2.8), Js(0.2), (-Js(2.0)), (-Js(4.2)), (-Js(6.3)), (-Js(8.4)), (-Js(10.3)), (-Js(12.3)), (-Js(14.2)), (-Js(16.2)), (-Js(18.3)), (-Js(20.1)), Js(100.7), Js(91.0), Js(84.7), Js(80.0), Js(76.0), Js(64.0), Js(51.2), Js(39.6), Js(28.2), Js(19.6), Js(14.4), Js(10.8), Js(7.7), Js(4.7), Js(1.9), (-Js(0.4)), (-Js(2.7)), (-Js(4.9)), (-Js(7.0)), (-Js(8.9)), (-Js(10.9)), (-Js(12.8)), (-Js(14.8)), (-Js(16.8)), (-Js(18.7)), Js(101.5), Js(93.0), Js(87.4), Js(83.3), Js(79.5), Js(67.6), Js(54.6), Js(43.0), Js(31.5), Js(22.3), Js(16.8), Js(12.5), Js(9.3), Js(6.0), Js(3.2), Js(0.7), (-Js(1.5)), (-Js(3.8)), (-Js(5.9)), (-Js(7.9)), (-Js(9.9)), (-Js(11.7)), (-Js(13.8)), (-Js(15.8)), (-Js(17.7)), Js(101.9), Js(94.1), Js(89.0), Js(85.1), Js(81.5), Js(70.0), Js(57.2), Js(45.7), Js(34.5), Js(25.1), Js(19.1), Js(14.2), Js(10.8), Js(7.5), Js(4.6), Js(1.9), (-Js(0.4)), (-Js(2.9)), (-Js(5.0)), (-Js(7.0)), (-Js(9.0)), (-Js(10.8)), (-Js(12.8)), (-Js(14.8)), (-Js(16.8)), Js(102.0), Js(94.8), Js(90.0), Js(86.3), Js(82.9), Js(72.0), Js(59.1), Js(48.0), Js(37.3), Js(28.3), Js(21.7), Js(16.3), Js(12.4), Js(8.9), Js(5.7), Js(3.0), Js(0.5), (-Js(2.0)), (-Js(4.2)), (-Js(6.1)), (-Js(8.0)), (-Js(10.0)), (-Js(11.9)), (-Js(13.9)), (-Js(15.9)), Js(102.1), Js(95.2), Js(90.8), Js(87.3), Js(84.1), Js(73.8), Js(61.0), Js(50.5), Js(40.3), Js(31.8), Js(24.7), Js(19.0), Js(14.5), Js(10.6), Js(7.1), Js(4.3), Js(1.7), (-Js(0.9)), (-Js(3.2)), (-Js(5.2)), (-Js(7.1)), (-Js(9.0)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), Js(102.2), Js(95.6), Js(91.3), Js(88.0), Js(85.0), Js(75.3), Js(62.6), Js(52.3), Js(42.7), Js(34.1), Js(27.0), Js(21.3), Js(16.3), Js(12.0), Js(8.5), Js(5.6), Js(2.8), Js(0.0), (-Js(2.3)), (-Js(4.3)), (-Js(6.2)), (-Js(8.2)), (-Js(10.2)), (-Js(12.2)), (-Js(14.1)), Js(102.3), Js(95.9), Js(91.8), Js(88.6), Js(85.8), Js(76.5), Js(64.0), Js(53.9), Js(44.3), Js(36.0), Js(29.3), Js(23.4), Js(18.0), Js(13.6), Js(9.7), Js(6.7), Js(3.8), Js(1.0), (-Js(1.6)), (-Js(3.6)), (-Js(5.5)), (-Js(7.5)), (-Js(9.5)), (-Js(11.4)), (-Js(13.2)), Js(102.4), Js(96.0), Js(92.0), Js(88.9), Js(86.2), Js(77.2), Js(65.0), Js(55.0), Js(45.7), Js(37.6), Js(31.0), Js(25.0), Js(19.8), Js(15.0), Js(10.8), Js(7.7), Js(4.8), Js(1.9), (-Js(0.9)), (-Js(3.0)), (-Js(4.8)), (-Js(6.8)), (-Js(8.9)), (-Js(10.8)), (-Js(12.5)), Js(102.5), Js(96.3), Js(92.5), Js(89.6), Js(87.3), Js(79.6), Js(68.2), Js(58.4), Js(49.4), Js(41.7), Js(35.4), Js(29.8), Js(24.5), Js(19.8), Js(15.0), Js(11.5), Js(8.2), Js(5.0), Js(2.0), (-Js(0.2)), (-Js(2.2)), (-Js(4.3)), (-Js(6.3)), (-Js(8.3)), (-Js(10.0)), Js(102.5), Js(96.5), Js(92.8), Js(90.0), Js(87.9), Js(80.5), Js(70.0), Js(60.8), Js(52.1), Js(44.8), Js(38.6), Js(33.0), Js(28.0), Js(23.4), Js(18.8), Js(14.8), Js(11.1), Js(7.8), Js(4.6), Js(1.9), (-Js(0.1)), (-Js(2.2)), (-Js(4.2)), (-Js(6.1)), (-Js(8.0)), Js(102.5), Js(96.5), Js(93.0), Js(90.3), Js(88.1), Js(81.0), Js(71.1), Js(62.5), Js(54.0), Js(46.7), Js(41.0), Js(35.7), Js(30.8), Js(26.0), Js(21.8), Js(17.5), Js(13.7), Js(10.0), Js(6.7), Js(3.7), Js(1.7), (-Js(0.4)), (-Js(2.3)), (-Js(4.4)), (-Js(6.3))]))
var.put('F51U', Js([Js(52.2), Js(41.6), Js(35.0), Js(30.3), Js(27.0), Js(23.8), Js(20.8), Js(17.8), Js(14.8), Js(12.0), Js(9.2), Js(6.6), Js(4.0), Js(1.2), (-Js(1.3)), (-Js(3.8)), (-Js(6.0)), (-Js(8.4)), (-Js(10.3)), (-Js(12.5)), (-Js(14.5)), (-Js(16.5)), (-Js(18.5)), (-Js(20.5)), (-Js(22.4)), (-Js(24.2)), (-Js(26.0)), (-Js(27.8)), (-Js(29.5)), (-Js(31.0)), (-Js(32.5)), Js(58.3), Js(46.7), Js(38.0), Js(32.1), Js(28.3), Js(25.2), Js(22.2), Js(19.3), Js(16.5), Js(13.4), Js(10.7), Js(8.0), Js(5.1), Js(2.5), (-Js(0.2)), (-Js(2.4)), (-Js(4.9)), (-Js(7.2)), (-Js(9.3)), (-Js(11.3)), (-Js(13.5)), (-Js(15.5)), (-Js(17.4)), (-Js(19.3)), (-Js(21.3)), (-Js(23.2)), (-Js(25.0)), (-Js(27.0)), (-Js(28.5)), (-Js(30.1)), (-Js(31.6)), Js(64.7), Js(52.4), Js(43.0), Js(35.3), Js(30.8), Js(27.6), Js(24.5), Js(21.3), Js(18.5), Js(15.6), Js(12.7), Js(9.9), Js(7.1), Js(4.4), Js(1.8), (-Js(0.8)), (-Js(3.1)), (-Js(5.5)), (-Js(7.7)), (-Js(9.8)), (-Js(12.0)), (-Js(14.0)), (-Js(15.9)), (-Js(17.8)), (-Js(19.8)), (-Js(21.6)), (-Js(23.4)), (-Js(25.5)), (-Js(27.1)), (-Js(28.9)), (-Js(30.7)), Js(68.0), Js(56.0), Js(46.3), Js(37.6), Js(32.6), Js(29.1), Js(26.0), Js(23.0), Js(20.0), Js(17.1), Js(14.0), Js(11.2), Js(8.8), Js(6.0), Js(3.2), Js(0.8), (-Js(1.7)), (-Js(4.1)), (-Js(6.2)), (-Js(8.4)), (-Js(10.4)), (-Js(12.7)), (-Js(14.6)), (-Js(16.5)), (-Js(18.6)), (-Js(20.4)), (-Js(22.2)), (-Js(24.2)), (-Js(26.0)), (-Js(27.9)), (-Js(29.8)), Js(70.5), Js(58.5), Js(48.8), Js(40.0), Js(34.7), Js(30.4), Js(27.2), Js(24.2), Js(21.2), Js(18.3), Js(15.2), Js(12.6), Js(10.0), Js(7.3), Js(4.6), Js(1.9), (-Js(0.5)), (-Js(3.0)), (-Js(5.2)), (-Js(7.4)), (-Js(9.6)), (-Js(11.7)), (-Js(13.8)), (-Js(15.6)), (-Js(17.7)), (-Js(19.6)), (-Js(21.3)), (-Js(23.3)), (-Js(25.0)), (-Js(27.0)), (-Js(29.0)), Js(72.3), Js(60.3), Js(50.8), Js(42.4), Js(36.7), Js(32.0), Js(28.4), Js(25.4), Js(22.4), Js(19.7), Js(16.5), Js(13.8), Js(11.0), Js(8.3), Js(5.7), Js(3.0), Js(0.6), (-Js(2.0)), (-Js(4.3)), (-Js(6.6)), (-Js(8.8)), (-Js(10.8)), (-Js(13.0)), (-Js(14.9)), (-Js(17.0)), (-Js(18.9)), (-Js(20.8)), (-Js(22.7)), (-Js(24.4)), (-Js(26.3)), (-Js(28.2)), Js(74.1), Js(62.3), Js(52.9), Js(45.1), Js(39.0), Js(34.5), Js(30.4), Js(27.0), Js(23.9), Js(21.0), Js(18.0), Js(15.3), Js(12.5), Js(9.7), Js(7.0), Js(4.4), Js(1.8), (-Js(0.7)), (-Js(3.2)), (-Js(5.4)), (-Js(7.7)), (-Js(9.8)), (-Js(12.0)), (-Js(14.0)), (-Js(16.0)), (-Js(17.9)), (-Js(19.9)), (-Js(21.8)), (-Js(23.7)), (-Js(25.6)), (-Js(27.5)), Js(75.4), Js(63.9), Js(54.9), Js(47.1), Js(40.8), Js(36.4), Js(32.2), Js(28.8), Js(25.2), Js(22.1), Js(19.3), Js(16.4), Js(13.8), Js(10.9), Js(8.1), Js(5.6), Js(2.9), Js(0.3), (-Js(2.2)), (-Js(4.5)), (-Js(6.7)), (-Js(8.9)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(17.0)), (-Js(19.1)), (-Js(21.0)), (-Js(22.8)), (-Js(24.8)), (-Js(26.8)), Js(76.4), Js(65.2), Js(56.3), Js(48.7), Js(42.4), Js(37.9), Js(33.9), Js(30.2), Js(26.6), Js(23.4), Js(20.3), Js(17.3), Js(14.8), Js(11.9), Js(9.1), Js(6.7), Js(3.9), Js(1.3), (-Js(1.2)), (-Js(3.6)), (-Js(5.8)), (-Js(7.9)), (-Js(10.0)), (-Js(12.2)), (-Js(14.2)), (-Js(16.2)), (-Js(18.2)), (-Js(20.2)), (-Js(22.0)), (-Js(24.0)), (-Js(26.0)), Js(77.4), Js(66.2), Js(57.6), Js(50.0), Js(43.7), Js(39.0), Js(35.1), Js(31.7), Js(27.8), Js(24.6), Js(21.3), Js(18.3), Js(15.7), Js(12.8), Js(10.0), Js(7.6), Js(4.8), Js(2.1), (-Js(0.4)), (-Js(2.8)), (-Js(5.0)), (-Js(7.1)), (-Js(9.2)), (-Js(11.3)), (-Js(13.4)), (-Js(15.4)), (-Js(17.5)), (-Js(19.4)), (-Js(21.3)), (-Js(23.2)), (-Js(25.1)), Js(79.5), Js(69.3), Js(60.9), Js(53.6), Js(47.7), Js(43.1), Js(39.2), Js(35.8), Js(32.0), Js(28.3), Js(24.9), Js(21.7), Js(18.8), Js(15.9), Js(13.1), Js(10.6), Js(7.9), Js(5.1), Js(2.2), Js(0.0), (-Js(2.2)), (-Js(4.3)), (-Js(6.6)), (-Js(8.9)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(17.0)), (-Js(19.0)), (-Js(21.0)), (-Js(22.9)), Js(80.7), Js(71.2), Js(63.0), Js(56.1), Js(50.2), Js(46.0), Js(42.1), Js(38.7), Js(35.0), Js(31.3), Js(27.8), Js(24.3), Js(21.2), Js(18.2), Js(15.5), Js(12.8), Js(10.0), Js(7.3), Js(4.7), Js(2.1), Js(0.0), (-Js(2.2)), (-Js(4.6)), (-Js(6.8)), (-Js(8.8)), (-Js(10.8)), (-Js(12.9)), (-Js(14.9)), (-Js(16.9)), (-Js(18.9)), (-Js(20.9)), Js(81.3), Js(72.6), Js(64.5), Js(58.0), Js(52.4), Js(48.0), Js(44.3), Js(40.7), Js(37.3), Js(33.8), Js(30.3), Js(27.0), Js(23.7), Js(20.5), Js(17.4), Js(14.7), Js(12.0), Js(9.2), Js(6.5), Js(4.0), Js(1.8), (-Js(0.4)), (-Js(2.8)), (-Js(5.0)), (-Js(7.0)), (-Js(9.0)), (-Js(11.0)), (-Js(13.0)), (-Js(15.0)), (-Js(16.8)), (-Js(18.6))]))
var.put('VGRID', Js([Js(0.01), Js(0.02), Js(0.03), Js(0.04), Js(0.05), Js(0.06), Js(0.07), Js(0.08), Js(0.09), Js(0.1), Js(0.15), Js(0.2), Js(0.3), Js(0.4), Js(0.5), Js(0.6), Js(0.7), Js(0.8), Js(0.9), Js(1.0), Js(1.2), Js(1.4), Js(1.6), Js(1.8), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(16.0), Js(17.0), Js(18.0), Js(19.0), Js(20.0), Js(22.0), Js(24.0), Js(26.0), Js(28.0), Js(30.0), Js(32.0), Js(34.0), Js(36.0), Js(38.0), Js(40.0), Js(42.0), Js(44.0), Js(46.0), Js(48.0), Js(50.0), Js(52.0), Js(54.0), Js(56.0), Js(58.0), Js(60.0), Js(62.0), Js(64.0), Js(66.0), Js(68.0), Js(70.0), Js(72.0), Js(74.0), Js(76.0), Js(78.0), Js(80.0), Js(81.0), Js(82.0), Js(83.0), Js(84.0), Js(85.0), Js(86.0), Js(87.0), Js(88.0), Js(89.0), Js(90.0), Js(91.0), Js(92.0), Js(93.0), Js(94.0), Js(95.0), Js(96.0), Js(97.0), Js(98.0), Js(98.2), Js(98.4), Js(98.6), Js(98.8), Js(99.0), Js(99.1), Js(99.2), Js(99.3), Js(99.4), Js(99.5), Js(99.6), Js(99.7), Js(99.8), Js(99.85), Js(99.9), Js(99.91), Js(99.92), Js(99.93), Js(99.94), Js(99.95), Js(99.96), Js(99.97), Js(99.98), Js(99.99)]))
var.put('ZGRI', Js([(-Js(3.71902)), (-Js(3.54008)), (-Js(3.43161)), (-Js(3.35279)), (-Js(3.29053)), (-Js(3.23888)), (-Js(3.19465)), (-Js(3.15591)), (-Js(3.12139)), (-Js(3.09023)), (-Js(2.96774)), (-Js(2.87816)), (-Js(2.74778)), (-Js(2.65207)), (-Js(2.57583)), (-Js(2.51214)), (-Js(2.45726)), (-Js(2.40892)), (-Js(2.36562)), (-Js(2.32635)), (-Js(2.25713)), (-Js(2.19729)), (-Js(2.14441)), (-Js(2.09693)), (-Js(2.05375)), (-Js(1.88079)), (-Js(1.75069)), (-Js(1.64485)), (-Js(1.55477)), (-Js(1.47579)), (-Js(1.40507)), (-Js(1.34076)), (-Js(1.28155)), (-Js(1.22653)), (-Js(1.17499)), (-Js(1.12639)), (-Js(1.08032)), (-Js(1.03643)), (-Js(0.99446)), (-Js(0.95416)), (-Js(0.91537)), (-Js(0.8779)), (-Js(0.84162)), (-Js(0.77219)), (-Js(0.7063)), (-Js(0.64335)), (-Js(0.58284)), (-Js(0.5244)), (-Js(0.4677)), (-Js(0.41246)), (-Js(0.35846)), (-Js(0.30548)), (-Js(0.25335)), (-Js(0.20189)), (-Js(0.15097)), (-Js(0.10043)), (-Js(0.05015))]))
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
calculo = var.to_python()