import './main';


describe('Test same structure as array method that should return true or false on passed arrays structures', () => {
    it('test case one', () => {
        expect([1,1,1].sameStructureAs([2,2,2])).toBe(true);
    });

    it('test case two', () => {
        expect([1,[1,1]].sameStructureAs([2,[2,2]])).toBe(true);
    });

    it('test case three', () => {
        expect([1,[1,1]].sameStructureAs([[2,2],2])).toBe(false);
    });

    it('test case four', () => {
        expect([1,[1,1]].sameStructureAs([2,[2]])).toBe(false);
    });

    it('test case five', () => {
        expect([[[],[]]].sameStructureAs([[[],[]]])).toBe(true);
    });

    it('test case six', () => {
        expect([[[],[]]].sameStructureAs([[1,1]])).toBe(false);
    });

    it('test case seven', () => {
        expect([1,[[[1]]]].sameStructureAs([2,[[[2]]]])).toBe(true);
    });

    it('test case eight', () => {
        expect([].sameStructureAs(1)).toBe(false);
    });

    it('test case nine', () => {
        expect([].sameStructureAs({})).toBe(false);
    });

    it('test case ten', () => {
        expect([1,'[',']'].sameStructureAs(['[',']',1])).toBe(true);
    });

    it('test case eleven', () => {
        expect([1,2].sameStructureAs([[3],3])).toBe(false);
    });
})
