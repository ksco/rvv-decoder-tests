rv_ireg_name_sym = [
    "zero", "ra", "sp", "gp", "tp", "t0",
    "s1", "a7", "s2", "t3",
]

rv_freg_name_sym = [
    "ft0", "fs0", "fa6", "fs8", "ft11",
]

rv_vreg_name_sym = [
    "v0",  "v1", "v31",
]

vm_name_sym = ["", ",v0.t"]

print("  .globl _start")
print("_start:")

# vd,(rs1),vm
for insn in [
    "vle8.v",
    "vle16.v",
    "vle32.v",
    "vle64.v",
    "vse8.v",
    "vse16.v",
    "vse32.v",
    "vse64.v",
]:
    for vd in rv_vreg_name_sym:
        for rs1 in rv_ireg_name_sym:
            for vm in vm_name_sym:
                print(f"{insn} {vd},({rs1}){vm}")
# vd,(rs1)
for insn in [
    "vlm.v",
    "vsm.v",
]:
    for vd in rv_vreg_name_sym:
        for rs1 in rv_ireg_name_sym:
            print(f"{insn} {vd},({rs1})")

# vd,(rs1),rs2,vm
for insn in [
    "vlse8.v",
    "vlse16.v",
    "vlse32.v",
    "vlse64.v",
    "vsse8.v",
    "vsse16.v",
    "vsse32.v",
    "vsse64.v",
]:
    for vd in rv_vreg_name_sym:
        for rs1 in rv_ireg_name_sym:
            for rs2 in rv_ireg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},({rs1}),{rs2}{vm}")

# vd,(rs1),vs2,vm
for insn in [
    "vluxei8.v",
    "vluxei16.v",
    "vluxei32.v",
    "vluxei64.v",
    "vloxei8.v",
    "vloxei16.v",
    "vloxei32.v",
    "vloxei64.v",
    "vsuxei8.v",
    "vsuxei16.v",
    "vsuxei32.v",
    "vsuxei64.v",
    "vsoxei8.v",
    "vsoxei16.v",
    "vsoxei32.v",
    "vsoxei64.v",
]:
    for vd in rv_vreg_name_sym:
        for rs1 in rv_ireg_name_sym:
            for vs2 in rv_vreg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},({rs1}),{vs2}{vm}")

# vd,vs2,vs1
for insn in [
    "vcompress.vm",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for vs1 in rv_vreg_name_sym:
                    print(f"{insn} {vd},{vs2},{vs1}")

# vd,vs2,vs1,v0
for insn in [
    "vadc.vvm",
    "vmadc.vvm",
    "vsbc.vvm",
    "vmsbc.vvm",
    "vmerge.vvm",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for vs1 in rv_vreg_name_sym:
                    print(f"{insn} {vd},{vs2},{vs1},v0")

# vd,vs2,vs1,vm
for insn in [
    "vadd.vv",
    "vsub.vv",
    "vwaddu.vv",
    "vwadd.vv",
    "vwsubu.vv",
    "vwsub.vv",
    "vwaddu.wv",
    "vwadd.wv",
    "vwsubu.wv",
    "vwsub.wv",
    "vand.vv",
    "vor.vv",
    "vxor.vv",
    "vsll.vv",
    "vsrl.vv",
    "vsra.vv",
    "vnsrl.wv",
    "vnsra.wv",
    "vmseq.vv",
    "vmsne.vv",
    "vmsltu.vv",
    "vmslt.vv",
    "vmsleu.vv",
    "vmsle.vv",
    "vminu.vv",
    "vmin.vv",
    "vmaxu.vv",
    "vmax.vv",
    "vmul.vv",
    "vmulh.vv",
    "vmulhu.vv",
    "vmulhsu.vv",
    "vdivu.vv",
    "vdiv.vv",
    "vremu.vv",
    "vrem.vv",
    "vwmulu.vv",
    "vwmulsu.vv",
    "vwmul.vv",
    "vsaddu.vv",
    "vsadd.vv",
    "vssubu.vv",
    "vssub.vv",
    "vaadd.vv",
    "vaaddu.vv",
    "vasub.vv",
    "vasubu.vv",
    "vsmul.vv",
    "vssrl.vv",
    "vssra.vv",
    "vnclipu.wv",
    "vnclip.wv",
    "vfadd.vv",
    "vfsub.vv",
    "vfwadd.vv",
    "vfwadd.wv",
    "vfwsub.vv",
    "vfwsub.wv",
    "vfmul.vv",
    "vfdiv.vv",
    "vfwmul.vv",
    "vfmin.vv",
    "vfmax.vv",
    "vfsgnj.vv",
    "vfsgnjn.vv",
    "vfsgnjx.vv",
    "vmfeq.vv",
    "vmfne.vv",
    "vmflt.vv",
    "vmfle.vv",
    "vredsum.vs",
    "vredand.vs",
    "vredor.vs",
    "vredxor.vs",
    "vredminu.vs",
    "vredmin.vs",
    "vredmaxu.vs",
    "vredmax.vs",
    "vwredsumu.vs",
    "vwredsum.vs",
    "vfredusum.vs",
    "vfredosum.vs",
    "vfredmin.vs",
    "vfredmax.vs",
    "vfwredusum.vs",
    "vfwredosum.vs",
    "vrgather.vv",
    "vrgatherei16.vv",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for vs1 in rv_vreg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{vs2},{vs1}{vm}")

# vd,vs2,vs1
for insn in [
    "vmand.mm",
    "vmnand.mm",
    "vmandn.mm",
    "vmxor.mm",
    "vmor.mm",
    "vmnor.mm",
    "vmorn.mm",
    "vmxnor.mm",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for vs1 in rv_vreg_name_sym:
                print(f"{insn} {vd},{vs2},{vs1}")

# vd,vs2,rs1,v0
for insn in [
    "vadc.vxm",
    "vmadc.vxm",
    "vsbc.vxm",
    "vmsbc.vxm",
    "vmerge.vxm",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for rs1 in rv_ireg_name_sym:
                print(f"{insn} {vd},{vs2},{rs1},v0")

# vd,vs2,fs1,v0
for insn in [
    "vfmerge.vfm",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for rs1 in rv_freg_name_sym:
                    print(f"{insn} {vd},{vs2},{rs1},v0")

# vd,vs2,rs1,vm
for insn in [
    "vadd.vx",
    "vsub.vx",
    "vrsub.vx",
    "vwaddu.vx",
    "vwadd.vx",
    "vwsubu.vx",
    "vwsub.vx",
    "vwaddu.wx",
    "vwadd.wx",
    "vwsubu.wx",
    "vwsub.wx",
    "vand.vx",
    "vor.vx",
    "vxor.vx",
    "vsll.vx",
    "vsrl.vx",
    "vsra.vx",
    "vnsrl.wx",
    "vnsra.wx",
    "vmseq.vx",
    "vmsne.vx",
    "vmsltu.vx",
    "vmslt.vx",
    "vmsleu.vx",
    "vmsle.vx",
    "vmsgtu.vx",
    "vmsgt.vx",
    "vminu.vx",
    "vmin.vx",
    "vmaxu.vx",
    "vmax.vx",
    "vmul.vx",
    "vmulh.vx",
    "vmulhu.vx",
    "vmulhsu.vx",
    "vdivu.vx",
    "vdiv.vx",
    "vremu.vx",
    "vrem.vx",
    "vwmulu.vx",
    "vwmulsu.vx",
    "vwmul.vx",
    "vsaddu.vx",
    "vsadd.vx",
    "vssubu.vx",
    "vssub.vx",
    "vaadd.vx",
    "vaaddu.vx",
    "vasub.vx",
    "vasubu.vx",
    "vsmul.vx",
    "vssrl.vx",
    "vssra.vx",
    "vnclipu.wx",
    "vnclip.wx",
    "vslideup.vx",
    "vslide1up.vx",
    "vslidedown.vx",
    "vslide1down.vx",
    "vrgather.vx",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for rs1 in rv_ireg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{vs2},{rs1}{vm}")

# vd,vs2,fs1,vm
for insn in [
    "vfadd.vf",
    "vfsub.vf",
    "vfrsub.vf",
    "vfwadd.vf",
    "vfwadd.wf",
    "vfwsub.vf",
    "vfwsub.wf",
    "vfmul.vf",
    "vfdiv.vf",
    "vfrdiv.vf",
    "vfwmul.vf",
    "vfmin.vf",
    "vfmax.vf",
    "vfsgnj.vf",
    "vfsgnjn.vf",
    "vfsgnjx.vf",
    "vfslide1up.vf",
    "vfslide1down.vf",
    "vmfeq.vf",
    "vmfne.vf",
    "vmflt.vf",
    "vmfle.vf",
    "vmfgt.vf",
    "vmfge.vf",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for fs1 in rv_freg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{vs2},{fs1}{vm}")

# vd,vs2,imm,v0
for insn in [
    "vadc.vim",
    "vmadc.vim",
    "vmerge.vim",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for imm in [-2, -1, 0, 1, 2]:
                print(f"{insn} {vd},{vs2},{imm},v0")

# vd,vs2,imm,vm
for insn in [
    "vadd.vi",
    "vrsub.vi",
    "vand.vi",
    "vor.vi",
    "vxor.vi",
    "vmseq.vi",
    "vmsne.vi",
    "vmsle.vi",
    "vmsgt.vi",
    "vsadd.vi",
    "vmsgtu.vi",
    "vsaddu.vi",
    "vmsleu.vi",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for imm in [-2, -1, 0, 1, 2]:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{vs2},{imm}{vm}")

# vd,vs2,uimm,vm
for insn in [
    "vsll.vi",
    "vsrl.vi",
    "vsra.vi",
    "vnsrl.wi",
    "vnsra.wi",
    "vssrl.vi",
    "vssra.vi",
    "vnclipu.wi",
    "vnclip.wi",
    "vslideup.vi",
    "vslidedown.vi",
    "vrgather.vi",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for imm in [0, 1, 2, 31]:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{vs2},{imm}{vm}")

# vd,vs1,vs2,vm
for insn in [
    "vmacc.vv",
    "vnmsac.vv",
    "vmadd.vv",
    "vnmsub.vv",
    "vwmaccu.vv",
    "vwmacc.vv",
    "vwmaccsu.vv",
    "vfmacc.vv",
    "vfnmacc.vv",
    "vfmsac.vv",
    "vfnmsac.vv",
    "vfmadd.vv",
    "vfnmadd.vv",
    "vfmsub.vv",
    "vfnmsub.vv",
    "vfwmacc.vv",
    "vfwnmacc.vv",
    "vfwmsac.vv",
    "vfwnmsac.vv",
]:
    for vd in rv_vreg_name_sym:
        for vs1 in rv_vreg_name_sym:
            for vs2 in rv_vreg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{vs1},{vs2}{vm}")

# vd,rs1,vs2,vm
for insn in [
    "vmacc.vx",
    "vnmsac.vx",
    "vmadd.vx",
    "vnmsub.vx",
    "vwmaccu.vx",
    "vwmacc.vx",
    "vwmaccsu.vx",
    "vwmaccus.vx",
]:
    for vd in rv_vreg_name_sym:
        for rs1 in rv_ireg_name_sym:
            for vs2 in rv_vreg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{rs1},{vs2}{vm}")

# vd,fs1,vs2,vm
for insn in [
    "vfmacc.vf",
    "vfnmacc.vf",
    "vfmsac.vf",
    "vfnmsac.vf",
    "vfmadd.vf",
    "vfnmadd.vf",
    "vfmsub.vf",
    "vfnmsub.vf",
    "vfwmacc.vf",
    "vfwnmacc.vf",
    "vfwmsac.vf",
    "vfwnmsac.vf",
]:
    for vd in rv_vreg_name_sym:
        for fs1 in rv_freg_name_sym:
            for vs2 in rv_vreg_name_sym:
                for vm in vm_name_sym:
                    print(f"{insn} {vd},{fs1},{vs2}{vm}")

# vd,vs1
for insn in [
    "vmv.v.v",
]:
    for vd in rv_vreg_name_sym:
        for vs1 in rv_vreg_name_sym:
            print(f"{insn} {vd},{vs1}")

# vd,rs1
for insn in [
    "vmv.v.x",
    "vmv.s.x",
]:
    for vd in rv_vreg_name_sym:
        for rs1 in rv_ireg_name_sym:
            print(f"{insn} {vd},{rs1}")

# vd,fs1
for insn in [
    "vfmv.v.f",
    "vfmv.s.f",
]:
    for vd in rv_vreg_name_sym:
        for fs1 in rv_freg_name_sym:
            print(f"{insn} {vd},{fs1}")

# vd,imm
for insn in [
    "vmv.v.i",
]:
    for vd in rv_vreg_name_sym:
        for imm in [-2, -1, 0, 1, 2]:
            print(f"{insn} {vd},{imm}")

# vd,vs2
for insn in [
    "vfsqrt.v",
    "vfrsqrt7.v",
    "vfrec7.v",
    "vmv1r.v",
    "vmv2r.v",
    "vmv4r.v",
    "vmv8r.v",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            print(f"{insn} {vd},{vs2}")

# vd,vs2,vm
for insn in [
    "vfclass.v",
    "vfcvt.xu.f.v",
    "vfcvt.x.f.v",
    "vfcvt.f.xu.v",
    "vfcvt.f.x.v",
    "vfcvt.rtz.xu.f.v",
    "vfcvt.rtz.x.f.v",
    "vfwcvt.xu.f.v",
    "vfwcvt.x.f.v",
    "vfwcvt.f.xu.v",
    "vfwcvt.f.x.v",
    "vfwcvt.f.f.v",
    "vfwcvt.rtz.xu.f.v",
    "vfwcvt.rtz.x.f.v",
    "vfncvt.xu.f.w",
    "vfncvt.x.f.w",
    "vfncvt.f.xu.w",
    "vfncvt.f.x.w",
    "vfncvt.f.f.w",
    "vfncvt.rod.f.f.w",
    "vfncvt.rtz.xu.f.w",
    "vfncvt.rtz.x.f.w",
    "vmsbf.m",
    "vmsif.m",
    "vmsof.m",
    "viota.m",
    "vzext.vf2",
    "vzext.vf4",
    "vzext.vf8",
    "vsext.vf2",
    "vsext.vf4",
    "vsext.vf8",
]:
    for vd in rv_vreg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for vm in vm_name_sym:
                print(f"{insn} {vd},{vs2}{vm}")

# rd,vs2,vm
for insn in [
    "vcpop.m",
    "vfirst.m",
]:
    for rd in rv_ireg_name_sym:
        for vs2 in rv_vreg_name_sym:
            for vm in vm_name_sym:
                print(f"{insn} {rd},{vs2}{vm}")

# rd,vs2
for insn in [
    "vmv.x.s",
]:
    for rd in rv_ireg_name_sym:
        for vs2 in rv_vreg_name_sym:
            print(f"{insn} {rd},{vs2}")

# fd,vs2
for insn in [
    "vfmv.f.s",
]:
    for fd in rv_freg_name_sym:
        for vs2 in rv_vreg_name_sym:
            print(f"{insn} {fd},{vs2}")

# vd,vm
for insn in [
    "vid.v",
]:
    for vd in rv_vreg_name_sym:
        for vm in vm_name_sym:
            print(f"{insn} {vd}{vm}")

# rd,rs1,rs2
for insn in [
    "vsetvl",
]:
    for rd in rv_ireg_name_sym:
        for rs1 in rv_ireg_name_sym:
            for rs2 in rv_ireg_name_sym:
                print(f"{insn} {rd},{rs1},{rs2}")

# vsetvli
for insn in [
    "vsetvli",
]:
    for rd in rv_ireg_name_sym:
        for rs1 in rv_ireg_name_sym:
            for e in [8, 16, 32, 64]:
                for m in ['f8', 'f4', 'f2', 1, 2, 4, 8]:
                    for vta in ['ta', 'tu']:
                        for vma in ['ma', 'mu']:
                            print(f"{insn} {rd},{rs1},e{e},m{m},{vta},{vma}")

# vsetivli
for insn in [
    "vsetivli",
]:
    for rd in rv_ireg_name_sym:
        for imm in [0, 1, 2, 31]:
            for e in [8, 16, 32, 64]:
                for m in ['f8', 'f4', 'f2', 1, 2, 4, 8]:
                    for vta in ['ta', 'tu']:
                        for vma in ['ma', 'mu']:
                            print(f"{insn} {rd},{imm},e{e},m{m},{vta},{vma}")

# csrs
for csr in [
    "vstart",
    "vxsat",
    "vxrm",
    "vcsr",
    "vl",
    "vtype",
    "vlenb"
]:
    print(f"csrrwi zero,{csr},1")